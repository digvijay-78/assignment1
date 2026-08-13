'''3.
Word Counter in Complaint Message

A customer care system wants to count how many words are present in a complaint message.

Input:
Enter complaint: Delivery was delayed again today

Output:
Total words: 5'''
n=input("=")
count=0
x=0
for i in range(len(n)):
	if n[i]==" ":
		x=0
	else:
		if x==0:
			count+=1
			x=1
print(count)