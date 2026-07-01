'''5. Next Prime ID Generator – Smart Version

A company gives prime numbered employee IDs to premium staff.

Manager enters current ID.
System must:

- Find next prime number after current ID
- Find difference between current ID and next prime

Write a program using loops.

Input:
20

Output:
Next Prime ID = 23
Gap = 3'''

m = int(input("="))
n = m + 1

while True:
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print("next id", n)
        break
    n += 1
diff=n-m
print("gap=",diff)
