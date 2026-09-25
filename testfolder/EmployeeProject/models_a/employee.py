s=[]
class Employee:
    def __init__(self) :
        self.employee_id=input("enter the employee id")
        self.employee_name=input("enter the employee name")
        self.department=input("enter the employee department")
        self.salary=int(input("enter the empolyee salary"))
        s.append(self)
    def display_emp(self):
        print("all employees:")
        for i in s:
            print(i.employee_id,i.employee_name,i.department,i.salary)
    def search (self):
        a=input("enter the id ")
        for i in s:
            if i.employee_id==a:
                print(i.employee_id,i.employee_name,i.department,i.salary)
            else:
                print("not in the list")
    def department_name(self):
        a=input("enter the department name:")
        for i in s:
            if i.department==a:
                print(i.employee_id,i.employee_name,i.department,i.salary)
        else:
            print("department not present")
    def high_paid(self):
        a=s[0]
        for i in s:
            if i.salary>a.salary:
                a=i
        print("highest salary")
        print(a.employee_id,a.employee_name,a.department,a.salary)        

