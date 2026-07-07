'''4.Spy Number Detector

A cybersecurity system flags special numeric codes.

A number is called a Spy Number if:
Sum of digits = Product of digits

Write a program to check whether the entered number is Spy Number or Not.

Input:
1124

Output:
Spy Number'''
n=int(input("="))
a=n
sum=0
product=1
for i in range(len(str(n))):
	di=n%10
	sum=sum+di
	product = product*di
        n//=10

if product==sum:
	print("spy no.")
else:
	print("not a spy no")	