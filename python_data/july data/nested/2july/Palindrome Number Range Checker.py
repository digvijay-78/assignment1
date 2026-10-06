'''6.
Palindrome Number Range Checker

A barcode verification system checks for palindrome numbers within a specific range.
The user enters starting and ending numbers.
The system displays all palindrome numbers using nested loops.

Input:
Enter starting number: 100
Enter ending number: 200

Output:
Palindrome Numbers are:
101
111
121
131
141
151
161
171
181
191'''
a,b=map(int,input("=").split( ))
for n in range(a,b+1):
    rev=0;tem=n
    for i in range(len(str(a))):
        d=n%10
        rev=rev*10+d
        n=n//10
    if tem==rev:
        print(tem)