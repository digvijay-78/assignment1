'''9.
Step Difference Number Analyzer

A mathematics research center studies hidden patterns inside numbers.
For every entered number, the system compares adjacent digits step by step.

Write a program to:

Find the absolute difference between every pair of adjacent digits
Display all step differences
Find the sum of all step differences
Find the largest step difference
If the sum of step differences is divisible by the number of digits, print Balanced Number
Otherwise print Unbalanced Number

Use loops wherever required.

Input:
57294
Output:
Step Differences: 2 5 7 5
Sum = 19
Largest = 7
Unbalanced Number
'''
n=int(input("="))
rev=0
sum=0
l=0
dig=len(n-1)
for i in range(len(str(n))):
	d=n%10
	rev=rev*10+d
	n=n//10
for i in range(len(str(rev))):
	d1=rev%10
	rev=rev//10
	d2=rev%10
	if rev!=0:
		diff=abs(d1-d2)
		print("differnce",diff,end=" ")
		sum=sum+diff
	if diff>l:
		l=diff
print()
print(sum)
print(l)
if diff%l==0
	print("balanced")
else:
	print("unbalanced")