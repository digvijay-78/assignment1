"""
7. Count Occurrence of a Particular Word

A company wants to analyze how frequently a particular keyword appears in a document.

Write a Python program that:

1. Reads a file named "article.txt".
2. Accepts a word from the user.
3. Counts how many times the given word occurs in the file.

Input File: article.txt

Python is simple.
Python is powerful.
Many developers use Python.
Python is popular.

Sample Input:

Enter word to search: Python

Expected Output:

Python occurs 4 times in the file.
"""


with open("article.txt","a+") as f:
    n=int(input("enter the no of lines"))
    for i in range(n):
        d=f.write(input("enter the data")+"\n")
char=input("Enter word to search: ").lower()
try :
    with open("article.txt","r") as f:
        c=0
        for k in f:
            m=k.split()
            for i in m:
                if i.lower()==char:
                    c+=1
        print(f"{char} occurs {c} times in the file.")
except FileExistsError:
    print("error")