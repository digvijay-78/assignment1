'''1.Vowel Counter in Customer Feedback

 A company wants to analyze customer feedback messages by counting how many vowels are present in the feedback.

Input: Enter feedback message: Hello Customer Service

Output: Total vowels: 8
'''
n=input("enter =").lower()
st="aeiou"
count=0

for i in n:
	if i in st:
		count+=1

print(count)