'''3.
Word Counter in Complaint Message

A customer care system wants to count how many words are present in a complaint message.

Input:
Enter complaint: Delivery was delayed again today

Output:
Total words: 5'''
n=input("=")
count=0
for i in n:
	if i==" ":
		count+=1

print(count+1)