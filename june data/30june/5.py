'''Number Stability Analyzer


A science lab studies whether digits are in increasing order.


Write a program using for-else loop:


- If every next digit is greater than previous print Stable Number

- Else Unstable Number


Input:

12359


Output:

Stable Number'''
n=int(input("="))
for i in range(len(str(n))):
    n1=n%10
    n=n//10
    n2=n%10
    if n1<n2:
        print("unstable")
        break
else:
    print("stable no.")