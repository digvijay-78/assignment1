"""6. Find the Longest Word

A document-processing application needs to identify the longest word in a text document.

Write a Python program that reads a file named "article.txt" and finds the longest word in the file.

Input File: article.txt

Python programming language is powerful.
Developers use Python for application development.

Expected Output:

Longest Word: programming
Length: 11"""


with open("article.txt","a+") as f:
    n=int(input("enter the no of lines"))
    for i in range(n):
        d=f.write(input("enter the data")+"\n")
try :
    with open("article.txt","r") as f:
        c=0
        l=""
        for k in f:
            m=k.split()
            for i in m:
                if len(i)>len(l):
                    c=len(i)
                    l=i
        print("Longest Word:",l,"\n","Length:",c)
except FileExistsError:
    print("error")