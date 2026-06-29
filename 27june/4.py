'''
4. Strong Number Checker

A digital lock opens only for strong numbers.

A strong number is a number whose sum of factorial of digits equals the number.

Example:
145 = 1! + 4! + 5!

Write a program using loops to check strong number.

Input:
145

Output:
Strong Number

n=int(input("="))
t=n

s=0
for i in range(len(str(n))):
    i=n%10
    fact=1
    for j in range (1,i+1):
        fact=fact*j
    n=n//10
    s=fact+s
if t==s:
    print("Strong Number")
else:
    print("not")'''

n=int(input("="))
t=n
i=0
s=0
j=1
while i<=n:
    i=n%10
    fact=1
    while j<=i+1:
        fact=fact*j
    n=n//10
    s=fact+s
if t==s:
    print("Strong Number")
else:
    print("not")