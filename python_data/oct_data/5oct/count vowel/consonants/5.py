"""5. Count Vowels and Consonants
A language-learning application wants to analyze the characters used in a paragraph.

Write a Python program that reads a file named "paragraph.txt" and counts:

1. Total number of vowels
2. Total number of consonants

Ignore numbers, spaces and special characters.

Input File: paragraph.txt

Python Programming is Interesting.

Expected Output:

Total Vowels: <display count>
Total Consonants: <display count>"""

with open ("paragraph.txt","a"
) as f:
    d=f.write(input(""))
try :
    with open("paragraph.txt","r") as f:
        v=0
        c=0
        for i in f:
            m=i.split()
            for k in m:
                for j in k :
                    if j.lower() in "aeiou":
                        v+=1
                    elif j.isalpha():
                        c+=1
        print(f"Total Vowels: <{v}>")
        print(f"Total Consonants: <{c}>")
except FileExistsError:
    print("error")