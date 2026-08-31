"""6.
=========================================
COMMON CHARACTER FINDER
=========================================
Enter two strings and find common characters.
Menu:
1. Enter First String
2. Enter Second String
3. Display Common Characters
4. Count Common Characters
5. Exit

Example:
String1: python
String2: typhoon

Output:
{p, t, h, o, n}"""

finder=set()
finder1=set()
while True:
    print("""Menu:
1. Enter First String
2. Enter Second String
3. Display Common Characters
4. Count Common Characters
5. Exit""")
    c=int(input("enter the choice "))
    match c:
        case 1:
            a=input("enter STRING 1")
            finder.update(a)
        case 2:
            a=input("enter string 2")
            finder1.update(a)
        case 3:
            print(finder&finder1)
        case 4:
            print(len(finder&finder1))
        case 5:
            break
        case _ :
            print("invalid")