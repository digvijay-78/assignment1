'''
3.
Replace Consecutive Duplicate Characters with Single Character
Data Compression System

A cloud storage company wants to reduce unnecessary repeated characters in text logs.

Write a Python program that replaces consecutive duplicate characters with a single occurrence.

Input:
aaabbbccccdddaa
Output:
abcda
'''
n=input("=")
c=n[0]
for i in range(1,len(n)):
    if n[i-1]!=n[i]:
        c=c+n[i]
print(c)