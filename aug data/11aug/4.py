'''4.
Find common elements in three sorted arrays.
Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
Note: can you take care of the duplicates without using any additional Data Structure?
Example 1:
Input:
n1 = 6; A = {1, 5, 10, 20, 40, 80}
n2 = 5; B = {6, 7, 20, 80, 100}
n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
Output: 20 80
Explanation: 20 and 80 are the only
common elements in A, B and C.'''
n = int(input("Enter size of first array: "))
a = []
for i in range(n):
    a.append(int(input("Enter element: ")))
n1 = int(input("Enter size of second array: "))
b = []
for i in range(n1):
    b.append(int(input("Enter element: ")))
n2 = int(input("Enter size of third array: "))
c = []
for i in range(n2):
    c.append(int(input("Enter element: ")))


#for i in range(len(a)):
#    if a[i] in b:
#        if a[i] in c:
#            z.append(a[i])
#print(z)
i = 0
j = 0
k = 0

print("Common elements:")

while i < len(a) and j < len(b) and k < len(c):

    if a[i] == b[j] and b[j] == c[k]:
        print(a[i], end=" ")
        i += 1
        j += 1
        k += 1

    elif a[i] < b[j]:
        i += 1

    elif b[j] < c[k]:
        j += 1

    else:
        k += 1