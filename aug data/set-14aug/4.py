"""4.
=========================================
FROZEN SET SUBJECT MANAGEMENT
=========================================
An institute offers fixed subjects:
Python
Java
MySQL
React
Spring Boot
These subjects cannot be modified after creation.

Menu:
1. Display Subjects
2. Search Subject
3. Count Subjects
4. Attempt to Add Subject
5. Exit

Requirements:
- Use Frozen Set.
- Show that modification is not allowed."""


subjects = frozenset(["Python", "Java", "MySQL", "React", "Spring Boot"])

while True:
    print("""
=========================================
FROZEN SET SUBJECT MANAGEMENT
=========================================
1. Display Subjects
2. Search Subject
3. Count Subjects
4. Attempt to Add Subject
5. Exit
""")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            print("Subjects:")
            print(subjects)

        case 2:
            sub = input("Enter subject to search: ")

            if sub in subjects:
                print("Subject Found")
            else:
                print("Subject Not Found")

        case 3:
            print("Total Subjects:", len(subjects))

        case 4:
            sub = input("Enter subject to add: ")

            try:
                subjects.add(sub)
            except AttributeError:
                print("Modification Not Allowed!")
                print("Frozen Set cannot be modified.")

        case 5:
            print("Program Ended")
            break

        case _:
            print("Invalid Choice")