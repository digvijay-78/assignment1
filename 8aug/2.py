'''2. First Repeating Number
=========================

Scenario

A security system logs employee IDs.

Find the first ID that repeats in the list.

Requirements

* Read N and list elements from user
* Find the first repeating number
* If no repeating number exists, display an appropriate message

Test Case 1

Input:
[10, 5, 3, 4, 3, 5]

Output:
First Repeating Number = 3

Test Case 2

Input:
[1, 2, 3, 4]

Output:
No Repeating Number Found'''

a=int(input("enter the len of list"))
arr=[]
for i in range(a):
    arr.append(int(input()))
p=[]
for i in range(len(arr)):
        c=0
        for k in range(len(arr)):
            if i!=k and  arr[i]==arr[k]:
                c+=1
        if c>0:
             p.append(arr[i])
             break
if len(p) == 0:
    print("No Non-Repeating Number Found")
else:
    print("First Repeating Number =", p[0])