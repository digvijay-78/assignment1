"""Assignment 1: Student Result Calculator
 A school wants to calculate the total marks and percentage of a student.
Create a class Student with the following attributes:
Student name
Roll number
Marks in English
Marks in Mathematics
Marks in Science
Create the following methods:
calculate_total() – Calculate the total marks.
calculate_percentage() – Calculate the percentage.
display_result() – Display student details, total, and percentage.
Expected output:
Student Name: Ajay
Roll Number: 101
Total Marks: 240
Percentage: 80.0%"""


class student:
    def accept(self,name,no,e,m,s):
        self.name=name
        self.no=no
        self.e=e
        self.m=m
        self.s=s
    def total(self):
        self.c=self.e+self.s+self.m
        
    def per(self):
        self.x=self.c/3
        
    def display(self):
        print(f"""Student Name:{self.name} 
Roll Number: {self.no}
Total Marks: {self.c}
Percentage: {self.x}%""")
        return self.c,self.x
n=input("enter the name")
r=int(input("enter the roll no"))
eng=float(input("enter the english marks"))
math=float(input("enter the maths marks"))
science=float(input("enter the science marks"))
o=student()
o.accept(n,r,eng,math,science)
o.total()
o.per()
o.display()