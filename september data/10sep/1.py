"""Assignment 1 — Age Calculator
Create a program that accepts the user's date of birth and calculates:
Current age in years
Completed months
Total number of days lived
Next birthday date
Number of days remaining for the next birthday
Input:
Enter DOB (DD-MM-YYYY): 15-08-1998
Expected Output:
Age: 28 years
Total Days Lived: XXXXX days
Next Birthday: 15-08-2027
Days Remaining: XX days
"""
from datetime import datetime,timedelta
a=input("enter the DOB")
today=datetime.now()
dt=datetime.strptime(a,"%d-%m-%Y")
age=today.year-dt.year
print("Age:",age)
total=(today-dt).days
print(total)
next_birthday = dt.replace(year=today.year+1)
print(datetime.strftime((next_birthday),"%d-%m-%Y"))
next=(next_birthday-today).days
print(next)
