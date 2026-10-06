"""4.
Assignment 10: Cyber Security (Strong Password Check)
A cybersecurity company considers a numeric password to be "strong" if every digit is even.
Task
Write a recursive function to check whether all digits of the given number are even.
Input 1
Enter Password:
248620
Output 1
Strong Password
Input 2
Enter Password:
248621
Output 2
Weak Password
"""

def found(n):
    if n==0:
        return 0
    if n%2==0:
        return 1+found(n//10)
    else:
        return 0+found(n//10)

n=int(input(""))
if len(str(n))==found(n):
    print(True)
else:
    print(False)
