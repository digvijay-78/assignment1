'''8.

 ATM Note Counter


A bank ATM dispenses ₹100 notes.


Write a program to:


- Read withdrawal amount

- Count how many ₹100 notes needed using loop


Input:

700


Output:

Notes = 7
'''
n=int(input("="))
a=0
for i in range(len(str(n))):
    d=n%100
    a=a+d
    if n<100:
        print("notes of hundred not requierd")
        break
    if n%100!=0:
        print(d,"need of other notes to")
        break
else:
    print(a)