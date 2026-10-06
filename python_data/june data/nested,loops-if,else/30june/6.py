'''6.

Next Prime Cabin Number Generator


A luxury hotel gives only prime numbered cabins to VIP guests.


Manager enters the last allotted cabin number.

System must find the next available prime cabin number.


Write a program using loops.


Input:

24


Output:

Next Prime Cabin = 29
'''
n=int(input("="))
m=n+1
sum=0
while True:
    if m<=1:
        print("not a prime no.")
    else:
        for i in range(2,n//2):
            if n%i==0:
                break
        else:
            print(m)
            break
        m+=1
                