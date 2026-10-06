
'''

---

**12. Multiplication of Digits**
A puzzle game calculates a score by multiplying all digits of a number together. After calculating the score, the game also checks whether the final score is even or odd to assign a bonus.
Write a program to **find the product of all digits of a number using loops and then check whether the result is even or odd**.

Input: 1234
Output: 24
Even'''


n=int(input("="))
sum=1
for i in range(len(str(n))):
	di=n%10
	n=n//10
	sum=sum*di
print (sum)
if sum%2==0:
	print ("even")
else:
	print("odd")


''''''
while n>0 :
    digit = n%10
    n = n//10
    product = product*digit
print(product)
if product%2 == 0:
    print("even")
else :
    print("odd")
'''


