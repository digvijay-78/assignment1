'''1.  Bank Customer Account Privacy System

A national bank is developing a secure customer portal where account
numbers should not be displayed completely on the screen. For security
reasons, the system should hide all digits except the last four digits
before showing them to users.

Conditions: - Display only the last 4 digits - Replace all previous
characters with *

Input: Enter account number: 123456789012

Output: Masked Account: ****9012'''
# a = input("Enter Account Number(Without Space): ")
# 
# for i in range(len(a)):
    # if ("a" <= a[i] <= "z") or ("A" <= a[i] <= "Z") or a[i]==" " or a[i]=="!@#$%^&()_+/-[]{ };"'' :
        # print("Only Digits Allowed (No Space)")
        # break
# else:
# 
    # for i in range(len(a) - 4):
        # print("*",end = "")
    # for i in range(len(a) - 4, len(a)):
        # print(a[i], end = "")
# 

a = input("Enter Account Number: ")

if a.isdigit():

    for i in range(len(a)-4):
        print("*", end="")

    for i in range(len(a)-4, len(a)):
        print(a[i], end="")

else:
    print("Only Digits Allowed (No Space)")