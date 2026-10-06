"""
3.
=========================================
WEBSITE VISITOR TRACKING SYSTEM
=========================================
A website stores unique visitor IDs.
Menu:
1. Add Visitor
2. Remove Visitor
3. Check Visitor
4. Display All Visitors
5. Count Unique Visitors
6. Clear Visitor Data
7. Exit

Requirements:
- Use a set to store visitor IDs.
- Duplicate visitor IDs should not be stored.
- Use add(), remove(), and membership operations."""

visitor=set()
while True:
    print("""1. Add Visitor)
2. Remove Visitor)
3. Check Visitor)
4. Display All Visitors)
5. Count Unique Visitor)
6. Clear Visitor Data)
7. Exit""")
    c=int(input("enter the choice "))
    match c:
        case 1:
            a=input("ENTER VISITOR ID: ")
            visitor.add(a)
        case 2:
            a=input("ENTER VISITOR ID: ")
            visitor.remove(a)
        case 3:
            a=input("ENTER VISITOR ID: ")
            if a in visitor:
                print("Visitor Found")
            else:
                print("Visitor Not Found")
        case 4:
            print("Visitors:", visitor)

        case 5:
            print("Unique Visitors:", len(visitor))

        case 6:
            visitor.clear()
            print("Visitor Data Cleared")

        case 7:
            break
        case _ :
            print("nahi chalega ")