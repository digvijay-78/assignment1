"""3. First Digit of Number
A university receives thousands of application IDs. The first digit of each ID represents the department code, 
so the admission software must read the first digit quickly.
Write a program to find the first digit of a number using loops.
Input:
53892

Output:
First Digit = 5"""


n=int(input("="))
t=n
sum=0
f=0
while n>0:
	sum=sum*10+n%10
	n=n//10

sum=sum%10
print(sum)

for i in range(len(str(t))):
	f=f*10+t%10
	t=t//10

f=f%10
print(f)

