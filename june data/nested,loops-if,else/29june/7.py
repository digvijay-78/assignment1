'''
7.
 Prime Sum Lucky Number

A lottery app checks if sum of digits is prime.

Write a program to:

- Find sum of digits
- If prime print Lucky Number
- Else Normal Number

Input:
4528

Output:
Sum = 19
Lucky Number
'''
import math
m = int(input("num : "))
sum = 0
while m>0 :
    d = m%10
    m = m//10
    sum = sum + d
print("sum =",sum)
n = sum
num = math.sqrt(n)
if n <= 1:
    print("Normal number")
else :
    i = 2 
    while i <= int(num) :
        if n%i == 0 :
            print("Normal number")
            break
        i+=1
    else :
        print("Lucky number")