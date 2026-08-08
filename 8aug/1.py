'''NOTE: In all programs, read the length and list elements from the user.

====================================================================

1. First Non-Repeating Number
   ====================================================================

Scenario

An online voting system stores vote IDs in a list.

Find the first vote ID that appears only once.

Requirements

* Read N and list elements from user
* Find the first non-repeating number
* If no such number exists, display an appropriate message

Test Case 1

Input:
[4, 5, 1, 2, 1, 2, 4]

Output:
First Non-Repeating Number = 5

Test Case 2

Input:
[7, 7, 8, 8]

Output:
No Non-Repeating Number Found

---'''
a=int(input("enter the len of list"))
arr=[]
for i in range(a):
    arr.append(int(input()))
p=[]
for i in range(len(arr)):
        c=0
        for k in range(len(arr)):
            if arr[i]==arr[k]:
                c=+1
                break
        if c==1:
             p.append(arr[i])
             break
if len(p) == 0:
    print("No Non-Repeating Number Found")
else:
    print("First Non-Repeating Number =", p[0])