"""5.
Hospital Record System (Search Digit)
A hospital stores patient IDs as numbers. The administrator wants to verify whether a specific digit exists 
in a patient ID.
Task
Write a recursive function to determine whether a given digit is present.
Input
Enter Patient ID:
5837264
Enter Digit:
7
Output
Digit Found"""
def found(n):
    if n==0:
        return
    if n%10==k:
        return 1
    return found(n//10)

n=int(input(""))
k=int(input(""))
if found(n)==1:
   print(True)
else:
    print(False)