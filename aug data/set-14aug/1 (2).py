'''1.
=========================================
STUDENT CLUB MEMBERSHIP SYSTEM
=========================================
A college has two clubs:
1. Coding Club
2. Robotics Club
Store student IDs of both clubs using sets.
Menu:
1. Add Student to Coding Club
2. Add Student to Robotics Club
3. Display Students in Coding Club
4. Display Students in Robotics Club
5. Find Students in Both Clubs
6. Find Students Only in Coding Club
7. Find Students Only in Robotics Club
8. Display All Unique Club Members
9. Display Total Unique Club Members
10. Exit
Requirements:
- Use two sets.
- Apply intersection, difference, and union operations.'''

coding=set()
robotics=set()
n=int(input("ENTER THE NO  OF CODING CLUB"))
for i in range(n):
    a=input("enter the student id")
    coding.add(a)
n=int(input("ENTER THE NO OF ROBOTICS CLUB STUDENTS: "))
for i in range(n):
    a=input("ENTER STUDENT ID: ")
    robotics.add(a)
print("Students in Coding Club:",coding)
print("Students in Robotics Club:",robotics)

#5va point
print(coding.intersection(robotics))
print(coding-robotics)
print(robotics-coding)
print(coding|robotics)
print(len(coding|robotics))
