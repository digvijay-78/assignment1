'''5.
Advanced Password Security Checker

A cyber security company wants to verify whether employee passwords are highly secure before giving system access.

Conditions: Password must:

Start with an uppercase letter
End with a digit
Contain at least 2 digits
Contain at least 1 special character (@ # $ % & *)
Must not contain spaces
Length should be between 8 and 15 characters

Input: Enter password: Python@45

Output: Secure Password'''
n=input("enter =")
l=len(n);di=0;d=0;upper=0;special=0;space=0

if "0"<= n[-1] <= "9":
	d=1
if "A" <= n[0] <= "Z":
	upper=1
for i in n:
	if i==" ":
		space=1
	elif i>="0"and i<="9":
		di+=1
	else:
		special=1
if 8<l<15 and upper==1 and d==1 and di>=2 and special==1 and space==0:
	print("secured")
else:
	print("not")