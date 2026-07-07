'''
Even Odd Difference Prime System

A smart scanner counts even and odd digits.

Write a program to:

- Count even digits
- Count odd digits
- Find difference
- Check whether difference is Prime or Not

Input:
123456

Output:
Even Count = 3
Odd Count = 3
Difference = 0
Not Prime
'''

import math
m = int(input("num : "))
ecount = 0 ; ocount = 0
while m > 0 :
    d = m%10
    m = m//10
    if d%2 == 0 :
        ecount += 1
    else :
        ocount += 1

print("even count =",ecount)
print("odd count =",ocount)

n = abs(ecount - ocount)
print("Difference =",n)

num = math.sqrt(n)
if n <= 1:
    print("not prime")
else :
    i = 2 
    while i <= int(num) :
        if n%i == 0 :
            print("not prime")
            break
        i+=1
    else :
        print("prime")