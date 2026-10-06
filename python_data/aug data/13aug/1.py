'''=====================================================================
QUESTION 1: EMPLOYEE SALARY ANALYSIS
====================================
A company wants to store employee details and generate salary reports using NamedTuple.
Fields:
emp_id, emp_name, department, salary
Requirements:
1. Read N employee details from the user and store them in a list of NamedTuples.
2. Display all employee details.
3. Find and display the employee with the highest salary.
4. Find and display the employee with the lowest salary.
5. Calculate and display the average salary of all employees.
6. Accept a department name from the user and display all employees belonging to that department.
Test Case:
Input:
Enter number of employees: 4

101 Rahul IT 50000
102 Priya HR 45000
103 Amit IT 70000
104 Neha Finance 60000

Enter department: IT

Expected Output:
Highest Salary Employee:
103 Amit IT 70000

Lowest Salary Employee:
102 Priya HR 45000

Average Salary:
56250.0

Employees in IT Department:
101 Rahul IT 50000
103 Amit IT 70000'''

from collections import namedtuple
company=namedtuple("company",["emp_id","emp_name","department","salary"])
n=int(input("enter no of employee =>"))
emp=[]
for i in range(n):
    print("enter details")
    id=int(input("enter emp.id>"))
    name=input("enter name")
    dept=input("enter department name ")
    sal=float(input("enter the salary"))
    s=company(id,name,dept,sal)
    emp.append(s)
print("details")
for x in emp:
    print("employe in ",x.department,"department:")
    print(x.emp_id ,x.emp_name ,x.department,x.salary)

c=emp[0]
for y in emp:
    if y.salary>c.salary:
        c=y
print("Highest Salary Employee:")
print(c.emp_id,c.emp_name,c.department,c.salary)

d=emp[0]
for y in emp:
    if y.salary<d.salary:
        d=y
print("Lowest Salary Employee:")
print(d.emp_id,d.emp_name,d.department,d.salary)

m=0
for k in emp:
    m=m+k.salary
avg=m/n
print("Average Salary:\n",avg )