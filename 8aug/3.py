'''3. Missing Number Detector
==========================

Scenario

Numbers from 1 to N should exist in a sequence, but one number is missing.

Requirements

* Read N and list elements from user
* Find the missing number
* Assume numbers belong to the range 1 to N+1

Test Case 1

Input:
[1, 2, 3, 5]

Output:
Missing Number = 4

Test Case 2

Input:
[2, 3, 4, 5]

Output:
Missing Number = 1

Test Case 3

Input:
[1, 2, 4, 5]

Output:
Missing Number = 3'''



a=int(input("enter the len of list"))
arr=[]
for i in range(a):
    arr.append(int(input()))
for i in range(len(arr)-1):
    if arr[i+1]-arr[i]!=1:
        print("Missing Value =", arr[i] + 1)
        break