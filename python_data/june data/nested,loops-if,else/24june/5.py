
'''

5. Palindrome Check
A number plate is considered special if it reads the same forward and backward. Such numbers are called palindromes.
Write a program to **check whether a given number is a palindrome using loops**.

Input: 121
Output: Palindrome
n=int(input(":"))
tem=n
sum=0
for i in range(len(str(n))):
	sum=sum*10+n%10
	n=n//10
if sum==tem:
	print (sum)	
else:
	print("error")
'''
n=int(input(":"))
tem=n
sum=0
while n>0:
	sum=sum*10+n%10
	n=n//10
if sum==tem:
	print (sum)	
else:
	print("error")


