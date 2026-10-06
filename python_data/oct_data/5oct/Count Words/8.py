"""8. Count Words Starting With a Particular Letter

A search engine wants to analyze words beginning with a particular character.

Write a Python program that:

1. Reads a file named "article.txt".
2. Accepts a character from the user.
3. Counts the number of words starting with that character.

Input File: article.txt

Python programming provides powerful features.
Programming helps developers build applications.

Sample Input:

Enter character: p

Expected Output:

Words starting with 'p': <display count>
"""

with open("article.txt","a+") as f:
    n=int(input("enter the no of lines"))
    for i in range(n):
        d=f.write(input("enter the data")+"\n")
char=input("enter character: ").lower()
try :
    with open("article.txt","r") as f:
        c=0
        for k in f:
            m=k.split()
            for i in m:
                if i.lower().startswith(char):
                    c+=1
        print(f"Words starting with {char}: {c}")
except FileExistsError:
    print("error")