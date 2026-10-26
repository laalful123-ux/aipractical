# AI Practical Answers Library
Search practical answers by **full question text** or keywords. `answers.show()` prints the stored code/steps.

## Install locally
```powershell
py -m pip install -e .
```

## Install from PyPI (after the package is published)
```powershell
py -m pip install aipractical
```
The short PyPI command will work only after the package owner publishes a release to PyPI. This ZIP does not publish it automatically.

## Your desired import pattern
```python
from aipractical import answers
answers.show("Implement Breadth-First Search (BFS) in Python to find the shortest path in an 8-puzzle. Use the given initial and goal configurations.")
```
You can paste the full question, not just its number. For similar/changed wording, use `answers.search("BFS shortest path 8 puzzle")`, then paste more words if multiple matches appear.

## Short terminal commands
```powershell
answers list
answers list --module 1
answers list --module 2
answers search "BFS shortest path 8 puzzle"
answers show "Create a Jira Automation rule with a trigger condition and action" --module 2
```

## Install from your GitHub repository after pushing
```powershell
py -m pip install git+https://github.com/YOUR_USERNAME/YOUR_REPO.git
```
Then use the `answers` terminal command. Use the exact repository URL you create.

## Included
- Module 1: 29 separate numbered Python answers, each also copied into `examples/module1/q01.py` through `q29.py`.
- Module 2: 34 Jira Cloud practical tasks with step-by-step checklists in `examples/module2/q01.txt` through `q34.txt`.
- Full question text stored in `src/aipractical/data.json`.
- Basic test suite in `tests/`.

## Dependencies for ML programs
The package itself uses only Python standard library. Some Module 1 ML solutions need scikit-learn and pandas:
```powershell
py -m pip install scikit-learn pandas
```
The ML examples use built-in Iris, Diabetes, and Digits datasets to avoid downloading California Housing during the exam.
Jira tasks require a Jira account, internet, and suitable project permissions. UI labels can vary.
