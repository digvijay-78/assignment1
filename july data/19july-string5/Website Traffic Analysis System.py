'''
4.

Find All Characters with Maximum Frequency
Website Traffic Analysis System

A web analytics company tracks user activity symbols in server logs.

The company wants to identify all characters having the maximum frequency in the given string.

Input:
aabbbccddd
Output:
b d
'''
n = input("=")

count = 0
c = ""

for i in n:
    if n.count(i) > count:
        count = n.count(i)
for i in n:
    if n.count(i) == count and i not in c:
        c = c + i + " "

print(c)