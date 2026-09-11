"""2.Employee Joining & Experience System
Create an employee experience calculator.
Read:
Employee name
Joining date
Current date
Calculate:
Total days worked
Total years worked
Total months approximately
Experience in Years Months Days
Whether employee has completed 1 year
Whether employee has completed 5 years
Example:
Enter employee name: Rahul
Enter joining date: 10-06-2021
Enter current date: 10-09-2026
Output:
Employee: Rahul
Joining Date: 10-06-2021
Experience: 5 Years 3 Months 0 Days
Total Days Worked: 1918
5 Years Completed: Yes"""
from datetime import datetime

emp=input("Enter employee name:")
join=input("Enter joining date:")
current=input("Enter current date:")

print("Employee:",emp)
print("Joining Date:",join)
dt=datetime.strptime(join,"%d-%m-%Y")
cdt=datetime.strptime(current,"%d-%m-%Y")
v=(cdt-dt)
d=(v.days)
year=v.days//365
rem=d%365
moths=rem//30
da=rem%30
print(f"Experience: {year} Years {moths} Months {da} Days")
print(v.days)
if year>=5:
    print("5 Years Completed: Yes")
elif year>=1:
    print("1 Years Completed: Yes")
else:
    print("0 Years Completed: Yes")




#from dateutil.relativedelta import relativedelta
# v = relativedelta(cdt, dt)

# print(v.years)
# print(v.months)
# print(v.days)
#print(f"Experience: {v.years} Years {v.months} Months {v.days} Days")