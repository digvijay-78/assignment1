'''QUESTION 2: STUDENT RESULT PROCESSING
=====================================
A training institute wants to manage student records using NamedTuple.
Fields:
roll_no, name, course, marks
Requirements:

1. Read N student records from the user and store them in a list of NamedTuples.

2. Display all student details.
3. Find and display the topper of the class.

4. Count and display the number of students scoring above 80 marks.


5. Calculate and display the average marks.

6. Accept a course name from the user and display all students enrolled in that course.

Test Case:

Input:
Enter number of students: 4

1 Ravi Python 85
2 Anjali Java 78
3 Karan Python 92
4 Pooja Testing 88

Enter course: Python

Expected Output:
Topper:
3 Karan Python 92

Students Above 80:
3

Average Marks:
85.75

Students in Python Course:
1 Ravi Python 85
3 Karan Python 92'''

from collections import namedtuple
student=namedtuple("student",["rollno","name","course","marks"])
n=int(input("enter no of students"))
students=[]
for i in range(n):
    print("enter details")
    r=int(input("enter rollno"))
    name=input("enter name")
    co=input("enter cource name").lower()
    m=float(input("enter marks"))
    s=student(r,name,co,m,)
    students.append(s)
print("Details")
for x in students:
    print(x.rollno,x.name,x.course,x.marks)

a=input("enter course:").lower()
t=0
m=0
abv=0
for y in students:
    if y.course ==a:
        if y.marks>m:
            m=y.marks
            t=y
    if (y.course==a) and (y.marks>=80):
        abv+=1

print("Topper:")
print(t.rollno,t.name,t.course,t.marks)
print("Students Above 80:\n",abv)

