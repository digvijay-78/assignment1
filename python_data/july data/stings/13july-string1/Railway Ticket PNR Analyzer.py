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

