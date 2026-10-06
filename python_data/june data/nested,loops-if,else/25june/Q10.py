'''10. Student ID Validity Checker (Count Odd Digits)
A school management system assigns numeric IDs to students. The administration wants to verify IDs by checking how many odd digits are present in each ID number. IDs with more odd digits are sent for manual review.

Write a program to count the number of odd digits in a given student ID using loops.

Input:
572943

Output:
Odd Digits Count = 3'''


n=int(input("= "))
t=n
count=0
c=0
for i in range(len(str(n-1))):
	d=n%10
	if d%2!=0:
		count=count+1
	n=n//10
print(count)
while t>0:
	d=t%10
	if d%2!=0:
		c=c+1
	t=t//10
print(c)