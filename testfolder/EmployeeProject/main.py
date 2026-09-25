from models_a.employee import Employee
from models_a.project import Project
v=[]
while True:
    k=int(input("enter the choice"))
    match k:
        case 1:
            print("1. Display All Employees")
            e1=Employee()
            e2=Employee()
            # e3=Employee()
            # e4=Employee()
            # e5=Employee()
            e1.display_emp()

        case 2:
            print("2. Search Employee by ID")
            e1=Employee()
            e2=Employee()
            # e3=Employee()
            # e4=Employee()
            # e5=Employee()
            e1.search()
        case 3 :
            print("Display Employees by Department")
            e1=Employee()
            e2=Employee()
            # e3=Employee()
            # e4=Employee()
            # e5=Employee()
            e1.department_name()
        case 4:
            print("4. Find Highest Paid Employee")
            e1=Employee()
            e2=Employee()
            # e3=Employee()
            # e4=Employee()
            # e5=Employee()
            e1.high_paid()
        case 5:
            print("5. Display Employee Projects")
            p1=Project()
            p2=Project()
            # p3=Project()
            # p4=Project()
            # p5=Project()
            p1.display()
        case 6:
            print("6. Find Highest Cost Project")
            p1=Project()
            p2=Project()
            # p3=Project()
            # p4=Project()
            # p5=Project()
            p1.highest()
        case 7:
            print("thankyou")
            break
        case _:
            print("invalid")