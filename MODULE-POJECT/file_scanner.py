from pathlib import Path
import os

path = Path(input("ENTER THE PATH: "))

ignore_folders = {
    "__pycache__",
    ".git",
    ".venv",
    "venv",
    "env",
    ".env",
    "node_modules"
}

if not path.exists():
    print("Invalid path")

elif path.is_file():
    print("single file")
    print("File:",path)

elif path.is_dir():
    print("Folder")
    print(path.name+"/")
    for root, folders, files in os.walk(path):
        for folder in folders:
            if folder in ignore_folders:
                folders.remove(folder)
        root=Path(root)
        level=len(root.relative_to(path).parts)
        indent="  "*level
        for folder in folders:
            print(indent + "├── " + folder + "/")

        for file in files:
            print(indent + "├── " + file)
    # for file in path.rglob("*.py"):
    #     # with open(file,"r") as f:
    #     #     code =f.read()
    #     print("\nPYTHON FILE:\n",file)
    #     print(code)
    # for file in path.rglob("*.py"):
    #     if any(folder in ignore_folders for folder in file.parts):
    #         continue

    #     print(file)