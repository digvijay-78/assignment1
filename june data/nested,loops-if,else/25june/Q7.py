'''7. Power of a Number
A scientific calculator app is used by engineering students for repeated multiplication operations. It should calculate the value of a number raised to a given power.
Write a program to calculate n raised to power p using loops.

Input:
2 5

Output:
32
'''
n=int(input("="))
m=int(input("="))
sum=1
i =1
'''
while i<=m:
	sum=sum*n
print(sum)'''

for i in (1,m+1):
		sum=sum*n
print(sum)
