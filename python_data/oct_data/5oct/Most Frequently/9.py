"""9. Find the Most Frequently Used Word

A content-analysis application wants to identify the most frequently used word in an article.

Write a Python program that reads a file named "article.txt" and finds the word that occurs the maximum number of times.

Input File: article.txt

Python is easy.
Python is powerful.
Python is popular.
Java is also popular.

Expected Output:

Most Frequently Used Word: Python
Frequency: 3"""

with open("article.txt","r")  as f:
    d=f.read()
    
c=d.split()
m=0
v=""
for i in c:
    k=c.count(i)
    if k>m:
        v=i
        m=k
print("Most Frequently Used Word:",v)
print("frequency",m)