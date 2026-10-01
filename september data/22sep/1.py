"""ASSIGNMENT 1 — EMPLOYEE MANAGEMENT SYSTEM
SCENARIO:
A company wants to maintain information about different types of employees.
Create the following class hierarchy:
Employee
|
+-------- Developer
|
+-------- Manager
REQUIREMENTS:
1. Create a parent class Employee.
Employee should contain:

* employee_id
* employee_name
* salary
2. Create Developer and Manager classes that inherit from Employee.
3. Employee should have a method:
display_details()
4. Developer should have:
programming_language
and a method:
write_code()
5. Manager should have:
team_size
and a method:
manage_team()
6. The child-class constructors must initialize parent-class data using super().
7. Override display_details() in both child classes.
8. From the overridden method, call the parent display_details() using super().
9. salary must be encapsulated.
Implement:
@property
@salary.setter
@salary.deleter
10. Salary setter must reject salary <= 0.
11. Read ALL employee information from the user.
INPUT REQUIREMENT:
Ask the user:
Enter Employee ID:
Enter Employee Name:
Enter Salary:
Enter Employee Type:
1. Developer
2. Manager
If Developer:
Enter Programming Language:
If Manager:
Enter Team Size:
SAMPLE INPUT:
Enter Employee ID: 101
Enter Employee Name: Rahul
Enter Salary: 45000
Enter Employee Type: 1
Enter Programming Language: Python
EXPECTED OUTPUT:
## Employee Details
Employee ID: 101
Employee Name: Rahul
Salary: 45000
Role: Developer
Programming Language: Python
Rahul is developing applications using Python.

"""


class Employee:
    def __init__(self,employee_id,employee_name,salary) :
        self.employee_id=employee_id
        self.employee_name=employee_name
        self.__salary=salary
    def display_details(self):
        print("Employee ID:",self.employee_id)
        print("Employee Name:",self.employee_name)
        print("Salary:",self.__salary)
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,salary):
        if salary<=0:
            print("invalid salary")
        else:
            self.__salary = salary
    @salary.deleter
    def salary(self):
        del self.__salary
class Developer(Employee):
    def __init__(self, employee_id, employee_name, salary,lang):
        super().__init__(employee_id, employee_name, salary)
        self.P_lang = lang
    def display_details(self):
        print("## Employee Details")
        super().display_details() 
        print("Role: Developer") 
        print("Programming Language:", self.P_lang)

    def write_code(self):
        print(f"{self.employee_name} is developing applications using {self.P_lang}.")
class Manager(Employee):
    def __init__(self,employee_id, employee_name, salary,team_size):
            super().__init__(employee_id,employee_name,salary)
            self.team_size = team_size
    def display_details(self):
            print("Employee Details")
            super().display_details() 
            print("Role: MANAGER") 
            print("Team Size:", self.team_size)
    def manager_team(self):
            print(f"{self.employee_name} is a Manager With team Size  {self.team_size}.")


id = int(input("Enter the Employee ID :"))
name = input("Enter The Employee Name:")
salary = int(input("Enter the Employee salary :"))
print("""Employee Type:
1. Developer
2. Manager""")
e_type = int(input("Enter Employee Type :"))
match e_type:
    case 1:
        lang = input("Enter Programming Language:")
        developer = Developer(id,name,salary,lang)
        developer.display_details()
        developer.display_details()
        developer.write_code()
    case 2:
        t_size = input("Enter Team Size:")
        manager = Manager(id,name,salary,t_size)
        manager.display_details()
        manager.manager_team()

    case _:
        print("Invalid Input")