"""2.
=========================================
ONLINE COURSE ENROLLMENT SYSTEM
=========================================
An institute offers:
1. Python Course
2. Java Course
Store enrolled student email IDs using sets.
Menu:
1. Enroll Student in Python
2. Enroll Student in Java
3. Display Python Students
4. Display Java Students
5. Find Students Enrolled in Both Courses
6. Find Students Enrolled Only in Python
7. Find Students Enrolled Only in Java
8. Check Enrollment in Python Course
9. Display Total Unique Students
10. Exit

Requirements:
- Use two sets.
- Use membership operator (in).
- Use union, intersection and difference operations"""

python=set()
java=set()
n=int(input("ENTER THE NO  OF python students"))
for i in range(n):
    a=input("ENTER STUDENT EMAIL")
    python.add(a) 

n=int(input("ENTER THE NO OF java  STUDENTS: "))
for i in range(n):
    a=input("ENTER STUDENT EMAIL: ")
    java.add(a)

print("Students in python \n",python)
print("java sutudents\n:", java)

print(python&java)
print(python-java)
print(java-python)
e=input("enter the email")
if e in python:
    print("in py")
else:
    print("not in python")
print(python|java)