'''1. Largest Digit in Number
A cybersecurity company checks numeric passwords used in smart lockers. To identify password strength, the system finds the highest digit present in the entered password. Higher digits indicate stronger variation in the password pattern.
Write a program to find the largest digit in a number using loops.

Input:
57294

Output:
Largest Digit = 9'''

n=int(input("="))
tem=n
max=1
while n>0:
	d=n%10
	if d>max:
		max=d
	n=n//10
print(max)
	

m=tem
max1=1
for i in range(len(str(m))):
	d=m%10
	if d>max1:
		max1=d
	m=m//10
print(max1) 
	

