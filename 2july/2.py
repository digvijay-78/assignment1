'''2.
Perfect Number Analyzer

A mathematics research system analyzes special numbers within a given range.
The user enters a starting number and ending number.
The system checks every number in that range and displays all Perfect Numbers using nested loops.

(A Perfect Number is a number whose sum of proper divisors is equal to the number itself.)

Input:
Enter starting number: 1
Enter ending number: 1000

Output:
Perfect Numbers are:
6
28
496'''
n=int(input("enter starting no. "))
m=int(input("Enter ending number"))

for i in range(n,m+1):
	sum=0
	for j in range(1,i//2+1):
		if i%j==0:
			sum=sum+j
	if sum==i:
		print("perfect no.'s are\n",i)
