'''2. Count Numbers Divisible by 7 Between Two Numbers

A company filters lucky coupon numbers divisible by 7.
Write a program using loops to count such numbers in range.

Input:
1 30

Output:
Count = 4'''
'''
n=int(input("="))
m=int(input("="))
count=0
for i in range (n,m+1):
	if i%7!=0:
		continue
	count=count+1
print(count)
'''
n=int(input("="))
m=int(input("="))
count=0
while n <=m+1:
	if n%7==0:
		count=count+1
	n=n+1
print(count)