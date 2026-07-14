'''3.
Character Occurrence Checker in Product Review

An e-commerce website wants to know how many times a particular character appears in a product review.

Input: Enter product review: this product is really good Enter character to check: o

Output: Character 'o' occurs: 4 times'''

n=input("enter =").lower()
ch=input("enter the char")
count=0
for i in n:
	if i==ch:
		count+=1
print(count)