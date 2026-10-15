# Flask Testability Analysis


This folder contains Python scripts for analyzing the testability of Flask 3.1.3 using the cloned Flask repository.

- `coverage.py` – Generates `flask_coverage_results.txt`, containing the Test Coverage.
- `ratio.py` – Generates `flask_line_count_results.txt`, containing the resulting ratio.
- `complexity.py` – Generates `flask_complexity_results.txt`, containing the cyclomatic complexity analysis results.

Each results file is generated when its corresponding Python script is executed.

## Note: all measurements were performed directly in the terminal. Later, Python scripts were added to the Flask repository in a new file named testability to save the results and demonstrate how the measurements could be generated and reproduced within the repository. The original approach and results remain the same; the additional files simply make the process easier to reproduce and preserve the output for reference. 
