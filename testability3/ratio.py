from pathlib import Path

folder = Path(__file__).parent
root = folder.parent
output = folder / "flask_line_count_results.txt"


def count_lines(directory, filtered=False):
    return sum(
        1 for file in directory.rglob("*.py")
        for line in file.read_text(encoding="utf-8").splitlines()
        if not filtered or (line.strip() and not line.lstrip().startswith("#"))
    )


with output.open("w", encoding="utf-8") as f:
    for filtered in (False, True):
        prod = count_lines(root / "src/flask", filtered)
        tests = count_lines(root / "tests", filtered)
        ratio = tests / prod if prod else 0

        f.write(f"{'Filtered' if filtered else 'All lines'}:\n")
        f.write(f"Production: {prod:,}\nTests: {tests:,}\n")
        f.write(f"Ratio: {ratio:.2f} ({ratio:.2%})\n\n")

print(f"Results saved to: {output.resolve()}")