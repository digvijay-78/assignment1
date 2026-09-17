"""Question 1: Employee Salary Management System
Scenario
A company wants to automate employee salary calculations. The HR department needs a system that calculates the 
gross salary of an employee by including allowances.
Requirements
Create a class named Employee with the following attributes:
employee_id
employee_name
basic_salary
Initialize the values using a constructor.
Calculations
HRA = 20% of Basic Salary
DA = 15% of Basic Salary
Gross Salary = Basic Salary + HRA + DA
Sample Input
Enter Employee ID : E101
Enter Employee Name : Rahul Sharma
Enter Basic Salary : 50000
Sample Output
------ Employee Salary Details ------
Employee ID      : E101
Employee Name    : Rahul Sharma
Basic Salary     : 50000.0
HRA              : 10000.0
DA               : 7500.0
Gross Salary     : 67500.0"""

class emp:
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal
    def hra(self):
        self.hra_sal=self.sal*20/100
    def da(self):
        self.da_sal=self.sal*15/100
    def gross(self):
        self.gross_sal=self.sal+self.hra_sal+self.da_sal
    def display(self):
        print(f"""------ Employee Salary Details ------
Employee ID      : {self.id}
Employee Name    : {self.name}
Basic Salary     : {self.sal}
HRA              : {self.hra_sal}
DA               : {self.da_sal}
Gross Salary     : {self.gross_sal}""")


id=input("enter the id")
name=input("enter the name")
salary=float(input("enter the salary"))
e=emp(id,name,salary)
e.hra()
e.da()
e.gross()
e.display()