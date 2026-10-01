"""Question 4: Student Result Processing System
Scenario
A college wants to automate result generation by calculating total marks, percentage, and grade.
Requirements
Create a class named Student with:
roll_number
student_name
marks1
marks2
marks3
Initialize the values using a constructor.
Calculations
Total = Marks1 + Marks2 + Marks3
Percentage = Total / 3
Grade Criteria
Percentage Grade
90 and above A
75 to 89 B
60 to 74 C
Below 60 D
Sample Input
Enter Roll Number : 101
Enter Student Name : Priya Sharma
Enter Marks in Subject 1 : 85
Enter Marks in Subject 2 : 90
Enter Marks in Subject 3 : 88
Sample Output
------ Student Result ------
Roll Number      : 101
Student Name     : Priya Sharma
Total Marks      : 263
Percentage       : 87.67
Grade            : B"""

class student:
    def __init__(self,roll,name,marks1,marks2,marks3):
        self.roll=roll
        self.name=name
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3
    def total(self):
        self.markstotal=self.marks1+self.marks2+self.marks3
    def percentage(self):
        self.per=self.markstotal/3
    def grade(self):
        if self.per>=90:
            self.g="A"
        if 89>=self.per>=75:
            self.g="B"
        if 74>=self.per>=60:
            self.g="C"
        else:
            self.g="B"
    def display(self):
        print(f"""------ Student Result ------
Roll Number      : {self.roll}
Student Name     : {self.name}
Total Marks      : {self.total}
Percentage       : {self.per}%
Grade            : {self.g}""")

r=input("enter the roll no")
n=input("enter the name")
m1=float(input("enter the marks1"))
m2=float(input("enter the marks2"))
m3=float(input("enter the marks3"))
s=student(r,n,m1,m2,m3)
s.total()
s.percentage()
s.grade()
s.display()