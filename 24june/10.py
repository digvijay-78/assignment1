'''

---

**10. Even Numbers Between Two Numbers**
A teacher wants to assign only even roll numbers for a special activity. The system should display all even numbers between two given numbers.
Write a program to **display all even numbers between two numbers using loops**.

Input: 10, 20
Output: 10 12 14 16 18 20'''

st=int(input("="))
ed=int(input("="))
for i in range(st,ed+1):
	if st%2==0:
		print(st,end=" ")
	st+=1






'''
st=int(input("="))
ed=int(input("="))

while st<=ed:
	if st%2==0:
		print(st, end = (" "))
	st+=1

'''





