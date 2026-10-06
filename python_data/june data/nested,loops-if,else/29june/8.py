'''
8. Largest Smallest Sum Prime Checker

A number analyzer finds largest and smallest digit.

Write a program to:

- Find largest digit
- Find smallest digit
- Find sum of both
- Check whether sum is Prime or Not

Input:
57294

Output:
Largest = 9
Smallest = 2
Sum = 11
Prime

'''
import math
m = int(input("num : "))
l = 1 ; s = 9
while m>0 :
    d = m%10
    m = m//10
    if d > l :
        l = d
    if d < s :
        s = d
print("smallest =",s)
print("largest =",l)

n = s + l 
print("sum",n)
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