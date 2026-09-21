from pathlib import Path
import ast

def analyze_file(path):

    path = Path(input("ENTER PYTHON FILE: "))

    with open(path, "r") as f:
        code = f.read()

    tree = ast.parse(code)
    function=[]
    classes=[]
    variable=[]
    paramter=[]
    imports=[]
    calls=[]

    print("\n========== IDENTIFIER REPORT ==========\n")

    for node in ast.walk(tree):
        if isinstance (node,ast.FunctionDef):
            function.append(node.name)
            for arg in node.args.args:
                paramter.append(arg.arg)

        elif isinstance(node,ast.ClassDef):
            classes.append(node.name)
            # for item in node.body:
            #     if isinstance(item, ast.FunctionDef):
            #         print("  Method:", item.name)

        elif isinstance(node,ast.Name):
            if isinstance(node.ctx, ast.Store):
                variable.append(node.id)

        elif isinstance(node,ast.Import):
            for name in node.names:
                imports.append(name.name)

        elif isinstance(node,ast.ImportFrom):
            for name in node.names:
                imports.append(name.name)

        elif isinstance(node,ast.Call):
            if isinstance(node.func,ast.Name):
                print("Called :",node.func.id)

            elif isinstance(node.func,ast.Attribute):
                print("Method called :",node.func.attr)
