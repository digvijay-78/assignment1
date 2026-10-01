"""ASSIGNMENT 5 – MENU-DRIVEN PAST DATE & TIME CALCULATOR
Create a menu-driven Python program that allows the user to calculate a date/time in the past by subtracting days,
weeks, hours,or minutes.
Menu
========== PAST DATE & TIME CALCULATOR ==========
1. Subtract Days
2. Subtract Weeks
3. Subtract Hours
4. Subtract Minutes
5. Exit
Enter your choice:
CASE 1 – Subtract Days
Input
Enter your choice: 1

Enter starting date (DD-MM-YYYY): 10-09-2026
Enter number of days to subtract: 100
Output
Starting Date : 10-09-2026
Days Subtracted : 100
Past Date : 02-06-2026
CASE 2 – Subtract Weeks
Input
Enter your choice: 2

Enter starting date (DD-MM-YYYY): 10-09-2026
Enter number of weeks to subtract: 6
Output
Starting Date : 10-09-2026
Weeks Subtracted : 6
Past Date : 30-07-2026
CASE 3 – Subtract Hours

Here the student must read both date and time.

Input
Enter your choice: 3

Enter date and time (DD-MM-YYYY HH:MM): 10-09-2026 10:30
Enter number of hours to subtract: 15
Output
Starting Date & Time : 10-09-2026 10:30
Hours Subtracted     : 15
Past Date & Time     : 09-09-2026 19:30
CASE 4 – Subtract Minutes
Input
Enter your choice: 4

Enter date and time (DD-MM-YYYY HH:MM): 10-09-2026 01:00
Enter number of minutes to subtract: 90
Output
Starting Date & Time : 10-09-2026 01:00
Minutes Subtracted   : 90
Past Date & Time     : 09-09-2026 23:30
CASE 5 – Exit
Enter your choice: 5

Thank you for using Past Date & Time Calculator!"""

from datetime import datetime,timedelta
while True:
    print("""Menu
========== PAST DATE & TIME CALCULATOR ==========
1. Subtract Days
2. Subtract Weeks
3. Subtract Hours
4. Subtract Minutes
5. Exit""")
    choice=int(input("enter choice"))
    match choice:
        case 1:
            print("Subtract Days")
            a=input("Enter starting date (DD-MM-YYYY):")
            b=int(input("Enter number of days to subtract: "))
            print("Starting Date :",a)
            print("Days Subtracted :",b)
            t=datetime.strptime(a,"%d-%m-%Y")
            past=t-timedelta(days=b)
            print("Past Date :",datetime.strftime((past),"%d-%m-%Y"))
        case 2:
            print("2. Subtract Weeks")
            a=input("Enter starting date (DD-MM-YYYY):")
            b=int(input("Enter number of days to subtract: "))
            print("Starting Date :",a)
            print("weeks Subtracted :",b)
            t=datetime.strptime(a,"%d-%m-%Y")
            past=t-timedelta(days=b*7)
            print("Past Date :",datetime.strftime((past),"%d-%m-%Y"))
        case 3:
            print("3. Subtract Hours")
            a=input("Enter starting date (DD-MM-YYYY):")
            b=int(input("Enter number of hours to subtract: "))
            print("Starting Date :",a)
            print("hours Subtracted :",b)
            t=datetime.strptime(a,"%d-%m-%Y")
            past=t-timedelta(seconds=b*3600)
            print("Past Date :",datetime.strftime((past),"%d-%m-%Y"))
        case 4:
            print("4. Subtract Minutes")
            a=input("Enter starting date (DD-MM-YYYY):")
            b=int(input("Enter number of minutes to subtract: "))
            print("Starting Date :",a)
            print("minutes Subtracted :",b)
            t=datetime.strptime(a,"%d-%m-%Y")
            past=t-timedelta(seconds=b*60)
            print("Past Date :",datetime.strftime((past),"%d-%m-%Y"))
        case 5:
            print("Thank you for using Past Date & Time Calculator!")
            break
        case _:
            print("invalid choice")