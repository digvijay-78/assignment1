"""
Assignment 4 – Menu-Driven Future Date Calculator
Develop a menu-driven Python program using the datetime module to calculate a future date.
The program should allow the user to add days, weeks, hours, or minutes to a given date/time.
Use timedelta for all date and time calculations.
Menu
========== FUTURE DATE CALCULATOR ==========
1. Add Days
2. Add Weeks
3. Add Hours
4. Add Minutes
5. Exit
Enter your choice:
Case 1 – Add Days
Read:
Starting date
Number of days
Input
Enter your choice: 1
Enter starting date (DD-MM-YYYY): 10-09-2026
Enter number of days to add: 100
Output
Starting Date : 10-09-2026
Days Added    : 100
Future Date   : 19-12-2026
Case 2 – Add Weeks
Read:
Starting date
Number of weeks
Input
Enter your choice: 2
Enter starting date (DD-MM-YYYY): 10-09-2026
Enter number of weeks to add: 4
Output
Starting Date : 10-09-2026
Weeks Added   : 4
Future Date   : 08-10-2026
Case 3 – Add Hours
For this case, the student should take date and time as input.
Input
Enter your choice: 3
Enter date and time (DD-MM-YYYY HH:MM): 10-09-2026 10:30
Enter number of hours to add: 15
Output
Starting Date & Time : 10-09-2026 10:30
Hours Added          : 15
Future Date & Time   : 11-09-2026 01:30
This case should test whether students understand that adding hours can change the date.
Case 4 – Add Minutes
Take date/time and number of minutes.
Input
Enter your choice: 4
Enter date and time (DD-MM-YYYY HH:MM): 10-09-2026 23:30
Enter number of minutes to add: 90
Output
Starting Date & Time : 10-09-2026 23:30
Minutes Added        : 90
Future Date & Time   : 11-09-2026 01:00
Students must correctly handle the change from 10 September → 11 September.
Case 5 – Exit
Enter your choice: 5
Thank you for using Future Date Calculator!
Complete Sample Run
========== FUTURE DATE CALCULATOR ==========
1. Add Days
2. Add Weeks
3. Add Hours
4. Add Minutes
5. Exit
Enter your choice: 1
Enter starting date (DD-MM-YYYY): 25-12-2026
Enter number of days to add: 15
Starting Date : 25-12-2026
Days Added    : 15
Future Date   : 09-01-2027
========== FUTURE DATE CALCULATOR ==========
1. Add Days
2. Add Weeks
3. Add Hours
4. Add Minutes
5. Exit
Enter your choice: 4
Enter date and time (DD-MM-YYYY HH:MM): 31-12-2026 23:30
Enter number of minutes to add: 90
Starting Date & Time : 31-12-2026 23:30
Minutes Added        : 90
Future Date & Time   : 01-01-2027 01:00
========== FUTURE DATE CALCULATOR ==========
1. Add Days
2. Add Weeks
3. Add Hours
4. Add Minutes
5. Exit
Enter your choice: 5
Thank you for using Future Date Calculator!"""
from datetime import datetime,timedelta
while True:
    print("""========== FUTURE DATE CALCULATOR ==========
1. Add Days
2. Add Weeks
3. Add Hours
4. Add Minutes
5. Exit""")
    choice=int(input("enter choice"))
    match choice:
        case 1:
            print("1. Add Days")
            a=input("Enter starting date (DD-MM-YYYY):")
            b=int(input("Enter number of days to add: "))
            dt=datetime.strptime(a,"%d-%m-%Y")
            day=dt+timedelta(b)
            print("Starting Date : ",dt)
            print("Days Added    : ",b)
            print("Future Date   : ",datetime.strftime((day),"%d-%m-%Y"))
        case 2:
            print("2. Add Weeks")
            a=input("Enter starting date (DD-MM-YYYY):")
            b=int(input("Enter number of weeka to add: "))
            t=datetime.strptime(a,"%d-%m-%Y")
            day=t+timedelta(b*7)
            print("Starting Date : ",t)
            print("weels Added    : ",b)
            print("Future Date   : ",datetime.strftime((day),"%d-%m-%Y"))
        case 3:
            print("Add Hours")
            a=input("Enter starting date (DD-MM-YYYY H(IN 12HR FORMAT):MIN):")
            b=int(input("Enter number of hours to add: "))
            t=datetime.strptime(a,"%d-%m-%Y %I:%M")
            day=t+timedelta(seconds=b*3600)
            print("Starting Date : ",t)
            print("Hours Added ",b)
            print("Future Date   : ",datetime.strftime((day),"%d-%m-%Y %I:%M"))
        case 4:
            print("4. Add Minutes")
            a=input("Enter starting date (DD-MM-YYYY H(IN 24HR FORMAT):MIN):")
            b=int(input("Enter number of mins to add: "))
            t=datetime.strptime(a,"%d-%m-%Y %H:%M")
            day=t+timedelta(seconds=b*60)
            print("Starting Date : ",t)
            print("Minutes Added        :",b)
            print("Future Date   : ",datetime.strftime((day),"%d-%m-%Y %I:%M"))
        case 5:
            print("")
            break
        case _:
            print("invalid choice")