"""Assignment 1 – Employee Bonus System
Create a parent class Employee with the following attributes:
employee_id
employee_name
salary
Create two child classes:
Developer
Manager
Requirements
Take employee details from the user.
Use super() to initialize the common attributes.
Create a method calculate_bonus() in the parent class.
Override calculate_bonus() in both child classes.
Developer gets 10% of salary as bonus.
Manager gets 20% of salary as bonus.
Display employee details, bonus and total salary.
Sample Input
Enter Employee ID: 101
Enter Employee Name: Rahul
Enter Salary: 50000
Enter Employee Type: Developer
Expected Output
----- Employee Details -----
Employee ID   : 101
Employee Name : Rahul
Salary        : 50000
Employee Type : Developer
Bonus         : 5000
Total Amount  : 55000"""


class Employee:
    def __int__(self,employee_id,employee_name,salary):
        self.employee_id=employee_id
        self.employee_name=employee_name
        self.salary=salary
    def calculate_bonus(self):
        self.total_amount=self.salary
        return self.total_amount
    def display(self):
        print(f"""----- Employee Details -----
Employee ID   : {self.employee_id}
Employee Name : {self.employee_name}
Salary        : {self.salary}""")
class Developer(Employee):
    def __int__(self, employee_id, employee_name, salary):
        super().__int__(employee_id, employee_name, salary)
    def calculate_bonus(self):
        super().calculate_bonus()
        self.total_amount= self.total_amount*0.9
    def display(self):
        super().display()
        print(f"""Employee Type : Developer
Bonus         : {self.total_amount-self.salary}""")
class Manager(Employee):
    def __int__(self, employee_id, employee_name, salary):
     super().__int__(employee_id, employee_name, salary)
    def calculate_bonus(self):
        super().calculate_bonus()
        self.total_amount= self.total_amount*0.8
    def display(self):
        super().display()
        print(f"""Employee Type : Manager
Bonus         : {self.total_amount-self.salary}""")

id=input("enter the id")
name=input("enter the name")
sal=int(input("enter the salary"))
m=input("enter the employee type:").lower()

if m=="developer":
    o=Developer()
elif m=="manager":
    o=Manager()
else:
    print("invalid employee type ")