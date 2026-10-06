'''
14.Floor Movement System (Elevator)
An elevator system takes the current floor and destination floor as input.

If current floor < destination → move upward and display floors
If current floor > destination → move downward and display floors
If both are same → display "Already on the same floor"

Write a program using if-elif-else and loops to simulate elevator movement.

Input: 1, 5
Output: 1 → 2 → 3 → 4 → 5

Input: 7, 3
Output: 7 → 6 → 5 → 4 → 3

Input: 4, 4
Output: Already on the same floor '''

current=int(input("= "))
destination=int(input("= "))
if current<destination:
		for i in range(current,destination+1):
			print(i)
elif current>destination:
		for i in range(current,destination-1,-1):
			print(i)


a=int(input("= "))
b=int(input("= "))
if a<b :
    i = a
    while i<=b :
        print(i,end="->" if i != b else " ")
        i+=1
elif a>b :
    i = a
    while i>=b :
        print(i,end="->" if i != b else " ")
        i-=1
else : 
    print("Both numbers are same")