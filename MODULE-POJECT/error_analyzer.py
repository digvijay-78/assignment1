from pathlib import Path
import ast
import subprocess
import sys

def analyze_error(path):
    path=Path(path)
    with open(path,"r") as f:
        code=f.read()
    try:
        ast.parse(code)
        print("\n========== ERROR REPORT ==========\n")
        print("no syntax error found")
    except SyntaxError as e:
        print("\n========== ERROR REPORT ==========\n")
        print("error type :",type(e).__name__)
        print("line :",e.lineno)
        print("Column:", e.offset)
        print("Message:", e.msg)
        print("Category: Syntax Error")
        return
    result =subprocess.run(
        [sys.executable,str(path)],
        capture_output=True,
        text=True
    )
    print("\n========== ERROR REPORT ==========\n")
    if result.returncode==0:
        print("no error found")
    else:
        lines=result.stderr.splitlines()
        error_line=lines[-1]
        error_type,message=error_line.split(":",1)
        error_type=error_type.strip()
        message=message.strip()
        print("error Type:",error_type)
        print("Message:",message)
        print("Category:","Runtime error")
        if error_type=="NameError":
            print("Suggestion: Check whether the variable is defined")

        elif error_type=="ZeroDivisionError":
            print("Suggestion: Check that you are not dividing by zero")

        elif error_type=="TypeError":
            print("Suggestion: Check the data types")

        elif error_type=="IndexError":
            print("Suggestion: Check the list index")

        else:
            print("Suggestion: Check the error message")
