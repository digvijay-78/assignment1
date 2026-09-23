# Enter number of test cases: 3

# ========== TEST CASE 1 ==========
# Enter input: 10
# 20
# Enter expected output: 30

# ========== TEST CASE 2 ==========
# Enter input: 5
# 7
# Enter expected output: 12

# ========== TEST CASE 3 ==========
# Enter input: 100
# 50
# Enter expected output: 150


# ========== TEST CASE 1 ==========

# Expected Output:
# 30

# Actual Output:
# 30

# ✅ PASSED
# ================================
#          FINAL RESULT
# ================================

# Total Test Cases : 3
# Passed           : 3
# Failed           : 0

# ✅ ALL TEST CASES PASSED

from pathlib import Path
import subprocess
import sys
def run_code(path):
    path=Path(path)
    result = subprocess.run(
        [sys.executable, str(path)],
        capture_output=True,
        text=True
    )

    