'''
6. Armstrong Number (3-digit)
In coding competitions, certain numbers are considered unique. A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
Write a program to **check whether a number is an Armstrong number using loops**.

Input: 153
Output: Armstrong'''

n=int(input(":"))
temp=n
sum=0
rem=0
for i in range(len(str(n))):
    sum=n%10
    rem=rem+sum*sum*sum
    n=n//10
if rem==temp:
	print("Armstrong")
else:
	print("not")
	




    while n>0 :
    digit = n%10
    n = n//10
    sum = sum + digit**3
print(sum)
if sum == m :
    print("Armstrong")
else : 
    print("Not Armstrong")

