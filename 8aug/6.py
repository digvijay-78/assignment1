'''6. Product Except Self
======================

Scenario

For every element, calculate the product of all other elements except itself.

Requirements

* Read N and list elements from user
* Create a new list containing products
* Display the result

Test Case 1

Input:
[1, 2, 3, 4]

Output:
[24, 12, 8, 6]

Test Case 2

Input:
[2, 3, 5]

Output:
[15, 10, 6]
'''

a=int(input("enter the len of list"))
arr=[]
for i in range(a):
    arr.append(int(input()))
p=[]
for k in range(a):
    c=1

    """p = []

for k in range(a):
    b = arr[:k] + arr[k+1:]
    c = math.prod(b)
    p.append(c)"""
    for j in range(a):
            if j!=k:
                 c=c*arr[j]
    p.append(c)
print(p)
