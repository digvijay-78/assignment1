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
for i in n:
    if "A" <= a <= "Z" or  "a" <= a <= "z":
        count=0
        if "0" <= b <= "9":
            count=0
            if i==" ":
                count=1
        else:
            count=1
            
    else:
        count=1
if len(n)>=10 and count==0:
    print("Valid Vehicle Number")
else:
    print("not Valid Vehicle Number")