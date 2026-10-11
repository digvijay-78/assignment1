"""4. Count Lines, Words and Characters in a File
A content management company wants to analyze the size of a text document.
Write a Python program that reads a file named "article.txt" and displays:

1. Total number of lines
2. Total number of words
3. Total number of characters

Input File: article.txt

Python is easy to learn.+Python is powerful.
Python is widely used in industry.

Expected Output:

Total Lines: 3
Total Words: 14
Total Characters: <calculate based on file content>
"""

with open("article.txt","w+") as f:
    d=f.write(input("enter ,if want to change line add '+' at the end of line"))
with open("article.txt","r") as f:
    line=0
    words=0
    ch=0
    for i in f:
        k=i.split("+")
        line+=len(k)
        for j in k :
            words+=len(j.split())
            for m in j:
                    ch+=1
    print(f"""Total Lines: {line}
Total Words: {words}
Total Characters: <{ch}>""")