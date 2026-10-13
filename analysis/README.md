Modifiability analysis – Section 2
This folder contains the measurement results used in Section 2 of our report.

Analysed version and scope
Flask: 3.1.3
Flask release commit: 22d924701a6ae2e4cd01e9a15bbaf3946094af65
Source directory: src/flask
The measurements include testing.py, which is excluded from the decomposition diagram in Section 1.3.

Tools
Python 3.11.9
Radon 6.0.1
Pylint 4.1.3
Astroid 4.3.4

Version information is saved in radon-version.txt and pylint-version.txt.

Files
| File | Contents |
| --- | --- |
| commit.txt | Analysed Flask release commit |
| cyclomatic-complexity.txt | Radon output |
| duplication.txt | Pylint output |
| file-changes.txt | Git history used for change coupling |
| file-change-results.txt | Results from the change-coupling script |
| radon-version.txt | Radon version |
| pylint-version.txt | Pylint, Astroid and Python versions |

The custom script is located at ../analyze_file_changes.py.

Cyclomatic complexity
Run from the Flask source checkout at the release commit listed above:

python -m radon cc src/flask -s -a


The saved result contains 385 blocks, including classes, functions and methods. Their average complexity is approximately 2.78.

Code duplication
The command used was:

python -m pylint src/flask --disable=all --enable=duplicate-code --reports=y > analysis\duplication.txt


This command was run in PowerShell from the Flask project root. No .pylintrc file was found in that root, and no Pylint-specific settings were found in pyproject.toml.
The output contains one duplicate-code message involving app.py and blueprints.py, but the summary reports zero duplicated lines. We therefore discuss the specific similarity and do not treat the reported 0.000% as a reliable overall duplication percentage.

Change coupling
The original history extraction command was:

git log --format="COMMIT %H" --name-only -- src/flask


The first and last commit records in the saved history are dated 1 June 2019 and 18 February 2026. The path restriction excludes history recorded only under earlier directory paths.

To run the analysis on the saved history, use this command from the analysis repository root, where analyze_file_changes.py is located:

python analyze_file_changes.py


The script reads analysis/file-changes.txt as UTF-16.

The history contains 439 commit records. The script counts only records with at least one listed Python file under src/flask, resulting in 382 analysed commits and 26 distinct Python file paths.

Each pair is counted once per commit. File moves and renames are not linked, and there is no additional filtering of formatting changes or large commits. The counts indicate co-change frequency, not proven dependencies or modification effort.

Tool documentation
Radon: https://radon.readthedocs.io/en/latest/intro.html
Pylint duplicate-code: https://pylint.readthedocs.io/en/latest/user_guide/messages/refactor/duplicate-code.html