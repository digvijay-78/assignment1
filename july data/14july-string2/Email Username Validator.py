'''1.
Email Username Validator

A company wants to check whether an employee email username is valid before creating an official account.

Conditions:
- Username should start with a letter
- Username can contain letters, digits, underscore (_)
- No spaces allowed
- Length should be between 5 and 12 characters

Input:
Enter username: ajay_123

Output:
Valid Username
'''
n=input("=")
a=n[0]
count=0;s=0
if ("a"<=a <="z") or ( "A"<=a and <="Z"):
	count=1
for i in n:
	if i==" ":
		s=1
if 5<= len(n) <= 12 and s==0 and count==1:
	print("valid")
else:
	print("unvalid")
