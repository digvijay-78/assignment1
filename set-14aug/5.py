"""5.
=========================================
LIBRARY ISBN MANAGER
=========================================
A library stores unique ISBN numbers of books.

Menu:
1. Add ISBN
2. Remove ISBN
3. Search ISBN
4. Display ISBN List
5. Count Books
6. Exit

Requirements:
- Use Set.
- Duplicate ISBNs are not allowed."""

id=set()
while True:
    print("""1. Add ISBN
2. Remove ISBN
3. Search ISBN
4. Display ISBN List
5. Count Books
6. Exit""")
    c=int(input("enter the choice "))
    match c:
        case 1:
            x=int(input("enter no of isbn you want to add"))
            for i in range(x):
                a=input("ENTER isbn ID: ")
                id.add(a)
        case 2:
            a=input("ENTER IBSN ID YOU WANT TO REMOVE: ")
            id.remove(a)
        case 3:
            a=input("ENTER IBSN ID YOU WANT TO search: ")
            if a in id:
                print("found")
            else:
                print("not found")
        case 4:
            print("ISBN list:",id)
        case 5:
            print("BOOK COUNT=",len(id))
        case 6:
            break
        case _:
            print("nahi chalega")