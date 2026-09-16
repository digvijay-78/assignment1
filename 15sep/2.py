"""Assignment 2: Employee Salary Calculator
A company wants to calculate an employee's gross salary.
Create a class Employee with the following attributes:
Employee ID
Employee name
Basic salary
HRA percentage
DA percentage
Create the following methods:
calculate_hra() – Calculate HRA.
calculate_da() – Calculate DA.
calculate_gross_salary() – Calculate gross salary.
display_salary() – Display employee salary details.
Formula:
HRA = Basic Salary × HRA Percentage / 100
DA = Basic Salary × DA Percentage / 100
Gross Salary = Basic Salary + HRA + DA"""
class emp:
    def accept(self,n,s,h,da):
        self.n=n
        self.s=s
        self.h=h
        self.da=da
    def hra(self):
        self.v=(self.s*self.h)/100
    def d(self):
            self.m=(self.s*self.da)/100
    def gross(self):
         self.n=self.s+self.v+self.m
    def display(self):
         return self.v,self.m,self.n
e=emp()
e.accept("yash",123,80,30)
e.hra()
e.d()
e.gross()
print(e.display())