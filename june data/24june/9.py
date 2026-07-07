'''
---

**9. Check All Digits Are Even**
A machine only accepts numbers where every digit is even. If any digit is odd, the number is rejected.
Write a program to **check whether all digits of a number are even using loops**.

Input: 2468
Output: All Even

Input: 2456
Output: Not All Even'''

n= int(input("="))
rem=0
count=0

for i in range(n,0):
	rem=n%10
        n=n//10
	if rem%2!=0:
		count=count+1
	
if count == 0:
	print("all even")
else:
	print("not")



while n>0 :
    digit = n%10
    n = n//10
    if digit % 2 != 0 :
        count+=1
if count == 0 :
    print("All Even")
else :
    print("Not all even")