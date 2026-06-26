
'''

---

**11. Count Occurrence of a Digit**
A system logs repeated digits in a number for pattern analysis and reporting.
Write a program to **count how many times a given digit appears in a number using loops**.

Input: Number = 122312, Digit = 2
Output: 3'''

n=int(input("="))
di=int(input(" ="))
count=0
for i in range(len(str(n))):
	rem=n%10
	n=n//10
	if rem/di==1:
		count+=1
print(count)


while n>0:
	rem=n%10
	n=n//10
	if rem/di==1:
		count+=1
print(count)


