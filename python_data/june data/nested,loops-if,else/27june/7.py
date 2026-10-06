'''7. Duck Number Checker

A verification system is used by an e-commerce company to validate promotional coupon numbers. Coupon numbers containing at least one zero in between digits are considered special duck numbers. However, if the number starts with zero, it is rejected immediately.

A duck number is a number that contains at least one zero but does not start with zero.

Example:
1023

Write a program using loops to check whether the entered number is a Duck number.

Input:
1023

Output:
Duck Number'''

n=input("=")
sum=0

For i in n:
	if n//10==0:
		print(rejected)
	i=n%10
	else:
		if i==0:
			print("duck no ")
			break 
		else:
			print("not a duck no ")
		rev=sum+i
		n=n//10








'''
n=int(input("="))
sum=0
for i in range (len(str(n))):
	i=n%10
	if i==0:
		print("duck no ")
		break 
	else:
		print("not a duck no ")
	rev=sum+i
	n=n//10'''