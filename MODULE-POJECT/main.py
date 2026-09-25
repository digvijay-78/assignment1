# PYCODE_INSPECTOR/
# │
# ├── pycode_inspector.py      # Entry point
# │
# ├── file_scanner.py         # Feature 1
# ├── code_analyzer.py        # Feature 2
# ├── quality_checker.py      # Feature 3
# ├── identifier_checker.py   # Feature 4
# ├── error_analyzer.py       # Feature 5
# ├── code_runner.py          # Feature 6
# └── report.py               # Feature 7

# | #     | File                    | Feature                                                  | Main modules                     |
# | ----- | ----------------------- | -------------------------------------------------------- | -------------------------------- |
# | **1** | `file_scanner.py`       | 📁 File & Folder Scan                                    | `pathlib`, `os`                  |
# | **2** | `code_analyzer.py`      | 🔍 Code Analysis                                         | `ast`                            |
# | **3** | `quality_checker.py`    | 🧠 Code Quality & Suggestions                            | `ast`                            |
# | **4** | `identifier_checker.py` | 🏷️ Identifier Analysis                                  | `ast`, `re`                      |
# | **5** | `error_analyzer.py`     | ❌ Error Detection & Explanation                          | `ast`, `subprocess`, `traceback` |
# | **6** | `code_runner.py`        | ▶️ Code Execution                                        | `subprocess`, `time`             |
# | **7** | `report.py`             | 📊 Statistics + Complete Terminal Report + Visualization | `ast`, `rich`                    |
# | —     | `pycode_inspector.py`   | 🚀 Entry Point / Controller                              | `sys`                            |


from identifier_checker import analyze_file
from error_analyzer import analyze_error
from code_runner import run_code
from report import generate_report



path = input("ENTER PYTHON FILE: ")

# analyze_file(path)
# analyze_error(path)
# run_code(path)
generate_report(path)