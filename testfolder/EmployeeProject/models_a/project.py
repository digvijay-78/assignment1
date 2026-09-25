p=[]
class Project:
    def __init__(self):
        self.project_id=input("enter the id")
        self.project_name=input("enter the name")
        self.employee_id=input("enter the employee id")
        self.project_cost=input("enter the cost")
        p.append(self)
    def display(self):
        for i in p:
            print(i.project_id,i.project_name,i.employee_id,i.project_cost)
    def highest(self):
        a=p[0]
        for i in p:
            if i.project_cost>a.project_cost:
                a=i
        print(a.project_id,a.project_name,a.employee_id,a.project_cost)
