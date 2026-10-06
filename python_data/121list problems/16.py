#16Sum of All Odd Length Subarray
arr = [1,4,2,5,3]
s=0

for i in range(len(arr)):
    for j in range(i, len(arr), 2):
        s += sum(arr[i:j+1])
print(s)