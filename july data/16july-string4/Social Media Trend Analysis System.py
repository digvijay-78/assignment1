'''
8.
Find the Second Highest Repeating Character in a String

Social Media Trend Analysis System

A social media company analyzes hashtags and user comments to identify trending character patterns.

The analytics team wants a Python program to find the character with the second highest frequency in a given string.

This helps detect secondary trending patterns in user activity.

Input:

aaabbbbccddeee

Output:

e

Explanation:

b occurs 4 times → highest
e occurs 3 times → second highest

Condition:

Program should work for both uppercase and lowercase letters.
Spaces should be ignored.
If no second highest frequency exists, print:
Second highest repeating character not found'''

n=input("=")
high=mid=0
ch1=ch2=""

for i in range(len(n)):
    count=n.count(n[i])

    if n[i]==ch1 or n[i]==ch2:
        continue

    if count > high:
        mid = high
        ch2 = ch1
        high = count
        ch1 = n[i]
    elif count > mid and count < high:
        mid = count
        ch2 = n[i]

if ch2 == "":
    print("Second highest repeating character not found")
else:
    print(ch2)
