'''
3.  Smart Chat Message Cleaner

A social media company noticed that users often enter messages with
unnecessary spaces. To improve readability and storage efficiency, the
system should remove extra spaces and keep only a single space between
words.

Input: Enter message: Java  is easy

Output: Cleaned Message: Java is easy
'''
s = input("Enter the string: ")
result = ""
for i in range(len(s)):
    if s[i] == " ":
        if i==0 or s[i-1]==" ":
            continue
    result+=s[i]
print(result) 



