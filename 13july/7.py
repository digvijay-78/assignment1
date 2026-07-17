'''7.
Vehicle Number Plate Checker

The traffic department wants to validate vehicle registration numbers.

Conditions:
- First 2 characters should be alphabets
- Next 2 should be digits
- Total length should be 10

Input:
Enter vehicle number: MP04AB1234

Output:
Valid Vehicle Number'''
n=input("enter =")
a=n[:2]
b=n[2:4]
count=0
space=0
for i in n:
    if "A" <= a <= "Z" or  "a" <= a <= "z":
        count=0
        if "0" <= b <= "9":
            count=0
        else:
            count =1
        if i==" ":
            space+=1
        else:
            count=0
            
    else:
        count=1
    if (len(n)-space)==10 and count==0:
        print("Valid Vehicle Number")
        break
    else:
        print("not Valid Vehicle Number")
        break
else:
    print("invalid")


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