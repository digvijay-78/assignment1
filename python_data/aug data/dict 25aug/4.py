"""
4.
=========================================
STUDENT GRADE ANALYSIS
======================
Store student marks in a dictionary.
students = {
"Ajay":78,
"Ravi":92,
"Neha":85,
"Aman":65
}
Write a program to:
* Find the student with highest marks.
* Find the student with lowest marks.
Sample Output:
Highest Marks : Ravi 92
Lowest Marks : Aman 65
"""
students = {
"Ajay":78,
"Ravi":92,
"Neha":85,
"Aman":65
}
for k,v in students.items():
    m=max(students.values())
    mi=min(students.values())
    if v>=m:
        print(k,m)
    if v<=mi:
        print(k,mi)


m = max(students.values())
mi = min(students.values())

for k, v in students.items():
    if v == m:
        print("Highest Marks :", k, m)
    if v == mi:
        print("Lowest Marks :", k, mi)