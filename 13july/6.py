'''6.
Railway Ticket PNR Analyzer

A railway department wants to verify whether a PNR number is valid.

Conditions:
- PNR must start with "PNR"
- Total length should be 12 characters
- Remaining characters should be digits

Input:
Enter PNR: PNR123456789

Output:
Valid PNR Number'''
n=input("enter =")
a=n[3:]

count=0
for i in n:
    if n[0]=="P" and n[1]=="N" and n[2]=="R":
        if "0"<= a <= "9":
            count=0
            if i==" ":
                count=1
        else:
            count=1
    else:
        count=1

if count==0 and len(n)>=12:
     print("valid")
else:
     print("not valid")



n = input("Enter vehicle number :")
l = len(n)
if len(n) == 10 and n[0] >= 'A' and n[0]<='Z' and n[1] >= 'A' and n[1]<='Z':
    if n[2] >= '0' and n[2] <= '9' and n[3] >= '0' and n[3] <= '9' :
        if n[l-1] >= '0' and n[l-1] <= '9' :
            print("Valid vehicle number")
        else :
            print("Invalid") 
    else :           
        print("Invalid")
else :
    print("Invalid")