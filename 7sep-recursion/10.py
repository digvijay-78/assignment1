"""6.
 Mobile Recharge System
A telecom company issues lucky recharge coupons only if the coupon number is prime.
Task
Write a recursive function to determine whether a given number is prime.
Input
Enter Coupon Number:
29
Output
Prime Number"""

def prime (n,i=2):
    if n<2:
        return 0
    if i==n:
         return 1
    if n%i==0:
            return 0
    return prime(n,i+1)

if prime(int(input("enter the no") ))==0:
     print("not prime")
else:
     print("prime")