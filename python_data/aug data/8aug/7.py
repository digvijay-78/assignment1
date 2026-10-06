'''7. Array Rotation Analyzer
==========================

Scenario

Rotate the array K times towards the right.

Requirements

* Read N and list elements from user
* Read K
* Rotate the array
* Display rotated array

Test Case 1

Input:
Array = [1, 2, 3, 4, 5]
K = 2

Output:
[4, 5, 1, 2, 3]

Test Case 2

Input:
Array = [10, 20, 30, 40]
K = 1

Output:
[40, 10, 20, 30]

---'''

n=int(input("enter size"))
arr=[]
i=0
while i<n:
    arr.append(int(input()))
    i=i+1
print(arr)
a=int(input ("enter the no. of rotation"))

po=arr[-a:]
arr = po + arr[:-a]
print(arr)


