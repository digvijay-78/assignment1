'''4.
Employee ID Validator

A company wants to validate employee IDs before storing them in the database.

Conditions:
- ID must start with "EMP"
- Total length should be 8
- Remaining characters should be digits only

Input:
Enter Employee ID: EMP10234

Output:
Valid Employee ID'''


n=input("enter =")
a=n[3:]

if len(n)==8 and n[0]=="E" and n[1]=="M" and n[2]=="P":
    count=1
    for i in a:
        if i < "0" or i > "9":
            count=0
            break
    if count==1:
        print("valid")
    else:
        print("invalid")
else:
     print("not valid")