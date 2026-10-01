empo=[]
greater=[]
class Emp:
    def __init__(self):
        self.employee_id=input("enter the id")
        self.name=input("enter the name")
        self.salary=float(input("enter the salary"))
        self.department=input("enter the department")
        print()
        empo.append(self)
    def display(self):
        print("\nAll Employees:\n")
        for i in empo:
            print(i.employee_id,i.name,i.salary,i.department)
    def greater_40k(self):
        print("\nEmployees with salary greater than 40000:\n")
        for i in empo:
            if i.salary>40000:
                greater.append(i)
        for i in greater:
            print(i.employee_id,i.name,i.salary,i.department)

    def it(self):
        print("\nEmployees from IT Department:\n")
        for i in  empo:
            if i.department.lower()=="it":
                print(i.employee_id,i.name,i.salary,i.department)
    def highest(self):
        a=0
        highest=[]
        for i in empo:
         if i.salary>a:
            a=i.salary
            highest.append(i)
        print("\nHighest Salary Employee:\n")
        print(highest[-1].employee_id,highest[-1].name,highest[-1].salary,highest[-1].department,"\n")
    def total(self):
        self.total_salary=0
        self.c=0
        for i in empo:
            self.total_salary+=i.salary
            self.c+=1
        print("Total Salary:\n",self.total_salary)
    def avg(self):
        if self.c!=0:
            self.avg_salary=self.total_salary/self.c
            
            print("Average salary:\n",self.avg_salary," \n")