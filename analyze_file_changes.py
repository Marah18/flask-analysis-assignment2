from collections import Counter
from itertools import combinations
from pathlib import Path

history_file = Path("analysis/file-changes.txt")

commit_count = 0
pair_counts = Counter()
file_counts = Counter()
current_files = set()


def process_commit(files):
    global commit_count

    if not files:
        return

    commit_count += 1

    for file in files:
        file_counts[file] += 1

    for first, second in combinations(sorted(files), 2):
        pair_counts[(first, second)] += 1


for line in history_file.read_text(encoding="utf-16").splitlines():
    line = line.strip()

    if line.startswith("COMMIT "):
        process_commit(current_files)
        current_files = set()
    elif line.startswith("src/flask/") and line.endswith(".py"):
        current_files.add(line)

process_commit(current_files)

print(f"Commits analyzed: {commit_count}")
print(f"Python files changed: {len(file_counts)}")
print("\nTop 15 co-changing file pairs:")

for (first, second), count in pair_counts.most_common(15):
    print(f"{count:4} | {first} | {second}")