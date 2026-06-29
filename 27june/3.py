'''3. Display Numbers Ending with 5

A supermarket tracks token numbers ending in 5.
Write a program using loops to display numbers ending with 5 between two numbers.

Input:
10 40

Output:
15 25 35'''
'''
n=int(input("="))
m=int(input("="))
sum=0
for i in range(n,m+1):
	if i%10==5:
		print(i,end=" ")
	i=i+1
'''
n=int(input("="))
m=int(input("="))
sum=0
while n<=m+1:
	if n%10==5:
		print(n,end=" ")
	n=n+1