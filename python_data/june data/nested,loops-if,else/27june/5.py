'''5. Harshad Number Checker

A number scanner is installed in a research laboratory where thousands of numeric access codes are tested every day. To identify mathematically balanced codes, the system checks whether the entered number qualifies as a Harshad number. Numbers passing this test are considered valid for the next stage of processing.

A Harshad number is a number that is exactly divisible by the sum of its digits.

Example:
18 → 1 + 8 = 9 and 18 ÷ 9 = 2

Write a program using loops to check whether the entered number is a Harshad number.

Input:
18

Output:
Harshad Number
n=int(input("="))
divisible=n
sum=0
for i in range (len(str(n))):
	i=n%10
	sum=sum+i
	n=n//10
if divisible%sum==0:
	print("Harshad Number")
else:
	print("not a Harshad Number")
'''
n=int(input("="))
divisible=n
sum=0
i=0
while i<=n:
	i=n%10
	sum=sum+i
	n=n//10
if divisible%sum==0:
	print("Harshad Number")
else:
	print("not a Harshad Number")