from pathlib import Path

path = Path(input("ENTER THE PATH: "))

if not path.exists():
    print("Invalid path")

elif path.is_file():
    print("single file")
    print("File:",path)

elif path.is_dir():
    print("Folder")
    item = list(path.iterdir())
    print("items:",item)

    for file in path.rglob("*.py"):
        print("PYTHON FILE:",file)
