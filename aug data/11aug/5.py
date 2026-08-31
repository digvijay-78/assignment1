'''5.
Rearrange the array in alternating positive and negative items
Given an unsorted array Arr of N positive and negative numbers.
Your task is to create an array of alternate positive and negative numbers
without changing the relative order of positive and negative numbers.
Note: Array should start with positive number.

Example 1:
Input:
N = 9
Arr[] = {9, 4, -2, -1, 5, 0, -5, -3, 2}
Output:
9 -2 4 -1 5 -5 0 -3 2
Example 2:
Input:
N = 10
Arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
Output:
5 -5 2 -2 4 -8 7 1 8 0'''


arr=[9, 4, -2, -1, 5, 0, -5, -3, 2]
pos=[]
ne=[]
for i in range(len(arr)):
    if arr[i]>=0:
        pos.append(arr[i])
    else:
        ne.append(arr[i])

result=[]
i=0
while i < len(pos) or i < len(ne):
    if i<len(pos):
        result.append(pos[i])
    if i<len(ne):
        result.append(ne[i])
    i=i+1
print(result)