'''5. Equilibrium Index Finder
===========================

Scenario

Find an index where:

# Sum of elements on the left side

Sum of elements on the right side

Requirements

* Read N and list elements from user
* Find equilibrium index
* If not found, display message

Test Case 1

Input:
[1, 3, 5, 2, 2]

Output:
Equilibrium Index = 2

Explanation:
1 + 3 = 2 + 2

Test Case 2

Input:
[1, 2, 3]

Output:
No Equilibrium Index Found'''

a=int(input("enter the len of list"))
arr=[]
for i in range(a):
    arr.append(int(input()))
r=0
l=0
for i in range(a):

    '''for i in range(n):
    l = sum(arr[:i])
    r = sum(arr[i+1:])'''
    for j in range(i):
        r=r+i

    for k in range(i+1,a):
        l=l+1

    if r==l:
        print(i)
    else:
             print("No Equilibrium Index Found")