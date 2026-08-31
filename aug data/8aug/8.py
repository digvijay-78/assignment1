'''8. Majority Element Detector
============================

Scenario

Find an element occurring more than N/2 times.

Requirements

* Read N and list elements from user
* Find majority element
* If not present, display appropriate message

Test Case 1

Input:
[2, 2, 1, 2, 3, 2, 2]

Output:
Majority Element = 2

Test Case 2

Input:
[1, 2, 3, 4]

Output:
No Majority Element Found
'''

n = int(input("Enter size: "))
arr = []

for i in range(n):
    x = int(input(f"Enter number {i+1} : "))
    arr.append(x)
print("\nInput:",arr)

c=1
for i in range(len(arr)):
    count=1
    for j in range(len(arr)):
        if i!=j and arr[i]==arr[j]:
            count+=1

    if count>n/2:
        print("majority ",arr[i])
        c=0
        break
if c==1:
        print("No Majority Element Found")
