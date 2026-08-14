'''2. Next Prime ID Generator

A multinational company auto-generates employee IDs in numeric sequence.
 Due to internal policy, only prime numbered IDs are assigned to new premium employees.

The HR manager enters the current last issued ID, and the software must search forward to find the next available prime number ID.

Write a program to find the first prime number after n.

Input:
14

Output:
Next Prime = 17'''
        

m = int(input("="))
n = m + 1

while True:
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print("prime no", n)
        break
    n += 1
