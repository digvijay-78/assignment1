'''
10.Zero Count Prime Scanner

A banking system checks account numbers.

Write a program to:

- Count zero digits
- Find sum of digits
- Add zero count and sum
- Multiply by smallest digit
- Check whether final result is Prime or Not

Input:
908406

Output:
Zero Count = 2
Sum = 27
Smallest Digit = 0
Final Result = 0
Not Prime
'''

import math
m = int(input("num : "))
count = 0
s = 9
sum = 0
while m>0 :
    d = m%10
    m= m//10
    sum = sum + d
    if d == 0 :
        count += 1
    if d < s :
        s = d         
n = (sum + count)*s      # n = final sum
print(count)
print(sum)
print(s)
print(n)


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