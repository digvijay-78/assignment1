'''4. Longest Consecutive Sequence
===============================
Scenario
Find the longest sequence of consecutive numbers present in the list.
Requirements

* Read N and list elements from user
* Find the length of the longest consecutive sequence
* Display the sequence length

Test Case 1

Input:
[100, 4, 200, 1, 3, 2]

Output:
Longest Consecutive Length = 4

Explanation:
Sequence = 1, 2, 3, 4

Test Case 2

Input:
[10, 11, 12, 20]

Output:
Longest Consecutive Length = 3'''

n = int(input("Enter size: "))
arr = []

for i in range(n):
    x = int(input(f"Enter number {i+1} : "))
    arr.append(x)
print("\nInput:",arr)

long=0
for ch in range(n):
    current = arr[ch]
    count=1
    while current+1 in arr:
        count+=1
        current+=1
    if count>long:
        long = count
print("Longest Consecutive Length:",long)