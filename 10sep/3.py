"""Assignment 3 — Date Difference Calculator
Create a program that accepts two dates and displays:
Enter first date: 10-09-2026
Enter second date: 25-12-2026
Display:

Difference in days
Difference in weeks
Difference in hours
Difference in minutes

Example:

Days Difference: 106
Weeks Difference: 15
Hours Difference: 2544
Minutes Difference: 152640
"""
from datetime import datetime,timedelta
a=input("Enter first date: ")
b=input("Enter second date: ")
d1=datetime.strptime(a,"%d-%m-%Y")
d2=datetime.strptime(b,"%d-%m-%Y")
v=d2-d1
print(v.days)
print(v.days//7)
print((v.days)*24)
print((v.days)*24*60)