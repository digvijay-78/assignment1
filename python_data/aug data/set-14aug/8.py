"""8.
=========================================
ALLOWED CHARACTER VALIDATOR
=========================================

Allowed characters are:
A-Z, a-z, 0-9

Store allowed characters in a Frozen Set.

Menu:
1. Enter Username
2. Validate Username
3. Display Allowed Characters
4. Exit

Requirements:
- Use Frozen Set.
- Username should contain only allowed characters.
-"""
allowed = frozenset("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")

username = ""

while True:
    print("\n1. Enter Username")
    print("2. Validate Username")
    print("3. Display Allowed Characters")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        username = input("Enter Username: ")

    elif choice == 2:
        valid = True

        for i in username:
            if i not in allowed:
                valid = False
                break

        if valid:
            print("Valid Username")
        else:
            print("Invalid Username")

    elif choice == 3:
        print("Allowed Characters:")
        print(allowed)

    elif choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")