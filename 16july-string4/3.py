'''
3. Find the First Non-Repeated Character

Railway Ticket Fraud Detection System

The railway department generates ticket reference IDs automatically.

Sometimes, due to technical issues, many characters get repeated inside the ticket ID.

The department wants a Python program that finds the first character that appears only once in the string.

Example 1

Input:
aabbccddefg
Output:


e

'''
a=input("=")
for i in range(len(a)):
    ch=a[i]
    count=0
    for j in range(len(a)):
          if ch==a[j]:
                count=count+1     
    if count ==1:
        print("First non repeated character :", a[i])
        break
else: 
    print("No Unique character found")