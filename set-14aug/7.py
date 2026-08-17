"""7.
=========================================
MISSING ALPHABET FINDER
=========================================

Enter a sentence and find which
alphabets are missing.

Menu:
1. Enter Sentence
2. Display Missing Alphabets
3. Count Missing Alphabets
4. Exit

Requirements:
- Use Set containing a-z."""

finder=set()
finder1=set("abcdefghijklmnopqrstuvwxyz")
while True:
    print("""Menu :
1. Enter Sentence
2. Display Missing Alphabets
3. Count Missing Alphabets
4. Exit""")
    c=int(input("enter the Choice "))
    match c:
        case 1:
            a=input("enter the Sentence")
            finder.update(a)
        case 2:
            print("missing values are ")
            print(finder1-finder)
        case 3:
            print(len(finder1-finder))
        case 4:
            break
        case _:
            print("nahi chalega ")
            