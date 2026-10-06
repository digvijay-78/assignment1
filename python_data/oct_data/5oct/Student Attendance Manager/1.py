"""1. Student Attendance Manager

A school wants to maintain the attendance of students in a text file named attendance.txt.

Each line contains:

RollNo,StudentName,Status

where Status is either Present or Absent.


Write a Python program to:

Accept attendance details for N students.
Store the details in attendance.txt.
Read the file and display:
Total students
Number of present students
Number of absent students
Attendance percentage
Sample Input
Enter number of students: 5

Enter Roll No: 101
Enter Student Name: Rahul
Enter Status: Present

Enter Roll No: 102
Enter Student Name: Priya
Enter Status: Absent

Enter Roll No: 103
Enter Student Name: Amit
Enter Status: Present

Enter Roll No: 104

Enter Student Name: Neha
Enter Status: Present

Enter Roll No: 105
Enter Student Name: Rohit
Enter Status: Absent
Expected Output
Attendance Report
-------------------------
Total Students: 5
Present Students: 3
Absent Students: 2
Attendance Percentage: 60.00%"""

n=int(input("Enter number of students:"))
for i in  range(n):
    with open("attendance.txt","a") as f:
        data=f.write(input("Enter Roll No:")+" ")
        data=f.write(input("Enter Student Name:")+" ")
        data=f.write(input("Enter Status:")+"\n")
try :
    print("""Attendance Report
-------------------------""")
    with open("attendance.txt","r") as f:
        
        p=0
        a=0
        for i in f:
            if "present" in i.lower():
                p+=1
            else:
                a+=1

        per=(p/n)*100
        print("Total Students:",n)
        print("Present Students:",p)
        print("Absent Students:",a)
        print(f"Attendance Percentage: {per:.2f}%")
except FileExistsError:
    print("error")