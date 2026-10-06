'''1. Triple Operation Prime Verification System


A cybersecurity company generates a security score from entered access code.


Write a program to:


- Find sum of digits of the number

- Reverse the number

- Find absolute difference between original number and reverse

- Add digit sum and difference

- Check whether final result is Prime or Not Prime


Input:

4215


Output:

Sum of Digits = 12

Reverse = 5124

Difference = 909

Final Result = 921

Not Prime'''
n=int(input("="))
a=n
sum=0
rev=0
m=n
for i in range(len(str(n))):
    d=m%10
    sum=sum+d
    m=m//10

for i in range(len(str(n))):
    d=n%10
    rev=rev*10+d
    n=n//10
diff=abs(rev-a)
final=diff+sum
if final<=1:
	print("not")
else:
	for i in range(2,final//2):
		if final%i==0:
			print("not a prime")
			break
	else:
		print("prime no.")
