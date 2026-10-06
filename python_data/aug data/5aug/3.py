'''3.
Industrial Sensor Peak Energy Monitoring System

Problem Statement

A factory machine records energy consumption at regular intervals.

A peak is defined as a value greater than or equal to its neighbors.

Tasks:

Find all peak energy values
Compute sum of squares of peak values
Compute average of peak values
Return difference between max peak and min peak
If no peaks, return -1

Test Case 1

Input:
energy = [20, 40, 30, 60, 50]

Output:
Peaks = [40, 60]
Sum of squares = 5200
Average = 50
Difference = 20

Test Case 2

Input:
energy = [10, 20, 15, 25, 20, 30]

Output:
Peaks = [20, 25, 30]
Sum of squares = 1525
Average = 25
Difference = 10

Test Case 3

Input:
energy = [5]

Output:
Peaks = [5]
Sum of squares = 25
Average = 5
Difference = 0'''

n=int(input("size"))
arr=[]
for i in range(n):
    arr.append(int(input()))
p=-1
c=[]
for i in range(n):
    if i==0:
        if n==1 or arr[i]>=arr[i+1]:
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
     sumsq=0
     navg=0
     
     for i in c:
          sumsq+=i**2
          navg+=i
     avg=navg//len(c)
     print("sum=",sumsq)
     print("avg=",avg)
     print("diffence",max(c)-min(c))

else:
     print("not found")