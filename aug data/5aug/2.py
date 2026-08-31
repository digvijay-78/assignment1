'''
2.
Smart City Traffic Peak Load Analyzer

Problem Statement

A smart city monitors traffic density at different time intervals in a day.

An element is called a peak traffic point if it is greater than or
 equal to its adjacent elements.

You are given an array traffic[] of size N.

Tasks:

Find all peak elements
Calculate the sum of all peak traffic values
Find the product of all peak traffic values
Return the maximum peak value

Note:
If only one element exists, it is the only peak.

Test Case 1

Input:
traffic = [10, 50, 30, 70, 60, 90, 80]

Output:
Peaks = [50, 70, 90]
Sum = 210
Product = 315000
Max Peak = 90

Test Case 2

Input:
traffic = [100, 200, 150, 180, 170]

Output:
Peaks = [200, 180]
Sum = 380
Product = 36000
Max Peak = 200

Test Case 3

Input:
traffic = [5]

Output:
Peaks = [5]
Sum = 5
Product = 5
Max Peak = 5'''

n=int(input("size"))
arr=[]
for i in range(n):
    arr.append(int(input()))
p=-1
c=[]
for i in range(n):
    if i==0:
        if n==1 or arr[i]>arr[i+1]:
            p=i
            c.append(arr[i])
            
    elif i==n-1:
        if arr[i]>=arr[i-1]:
            p=i
            c.append(arr[i])
            
    else:
        if arr[i]>=arr[i-1] and arr[i]>=arr[i+1]:
                p=i
                c.append(arr[i])
             
if p!=-1:
     print("peak index",p)
     print("peak index",arr[p])     
     print("peak =",c)
     sum=0
     product=1
     for i in c:
          sum+=i
          product=product*i
     print("sum=",sum)
     print("product=",product)
     print("max peak",max(c))

else:
     print("not found")