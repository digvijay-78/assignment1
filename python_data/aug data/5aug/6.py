'''6.

A security system logs employee entry IDs during a day.

Only prime-numbered IDs are considered valid VIP entries.

Tasks:

Extract all prime IDs from the list
Find the sum of prime IDs
Find the maximum prime ID
Count how many prime entries exist

Input:
A list of integers (may contain duplicates and non-prime numbers)

Example 1

Input:
[12, 5, 7, 9, 11, 14, 17]

Output:
Prime IDs = [5, 7, 11, 17]
Sum = 40
Max = 17
Count = 4

Example 2

Input:
[4, 6, 8, 10]

Output:
Prime IDs = []
Sum = 0
Max = -1
Count = 0
'''
import math
n=int(input("size"))
arr=[]
for i in range(n):
    arr.append(int(input()))
prime=[]
sum=0

for i in range(len(arr)):
    if arr[i]<=1:
        continue
    isprime=1
    for j in range(2,int(math.sqrt(arr[i]))+1):
        if arr[i]%j==0:
            isprime=0
            break
    if isprime==1:
            prime.append(i)
            sum+=arr[i]
if len(prime)==0:
     m=-1
else:
    m=max(prime)
c=len(prime)
print(prime,sum,m,c)