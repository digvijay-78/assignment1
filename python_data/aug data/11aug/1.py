'''1. Count Pairs with Difference K
A company records the ages of employees. Find how many pairs of employees have an age
difference exactly equal to K.
Problem Statement:
Given an array of employee ages and an integer K, count the number of pairs whose absolute difference is K.

Exampe:
Input:

N = 5
K = 2
ages[] = {1, 5, 3, 4, 2}

Output:

3

Explanation:

(1,3), (3,5), (2,4)'''
a=int(input("N="))
k=int(input("K="))
ages=[]
print("enter array elements:")
for i in range(a):
    ages.append(int(input()))
print()

c=0
for i in range(a):
    for j in range(i+1,a):
        if abs(ages[i]-ages[j])==k:
            c+=1
print(c)