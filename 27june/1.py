'''1. Product of Odd Numbers up to N

A puzzle game rewards players by multiplying odd numbers up to n.
Write a program using loops to find product of odd numbers.

Input:
5

Output:
15'''
n=int(input("="))

s=1
m=1
for i in range(1,n+1):
	if i%2==0:
		continue
	s=s*i
print(s)
i=1
while i<=n:
	if i%2==0:
		continue
	m=m*i
print(m)