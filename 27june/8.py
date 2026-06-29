'''8.
Mirror Difference Transaction Verification System
A multinational banking company processes thousands of daily transaction IDs. To detect suspicious patterns and validate system-generated IDs,
 the security software performs a Mirror Difference Verification Test.
For every entered transaction ID:

Reverse the digits of the transaction ID

Find the absolute difference between the original ID and the reversed ID


Count the total number of digits in the difference

Apply the following conditions using if-elif-else:

If the difference is 0, print Perfect Match

Else if the difference is divisible by 9, print Verified

Else print Rejected


Write a program to automate this verification process using loops and conditional statements.
Input:
4215
Output:
Reverse = 5124Difference = 909Digits = 3Verified
Input:
1221
Output:
Reverse = 1221Difference = 0Digits = 1Perfect Match
Input:
1234
Output:
Reverse = 4321Difference = 3087Digits = 4Verified
'''
n=int(input("="))
r=n
re=0
for i in range(len(str(n))):
	d=n%10
	re=re*10+d
	n=n//10
difference =re-r
dif=difference 
count=0
rev=0
for i in range(len(str(difference))):
	d=difference%10
	rev=rev*10+d
	difference =difference //10
	count=count+1
if dif==0:
	 print("reverse={} difference= {} digits= {}Perfect Match".format(re,dif,count))
elif dif%9==0:
	 print("reverse= {} difference= {} digits={}verified".format(re,dif,count))
else:
	print("rejected")
