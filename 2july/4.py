'''4.
Armstrong Number Finder

A digital number analysis system checks for Armstrong numbers within a range.
The user enters starting and ending numbers.
The system finds all Armstrong numbers using nested loops.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Armstrong Numbers are:
1
153
370
371
407'''
a=int(input("="))
b=int(input("="))
for n in range(a,b+1):
    sum=0
    tem=len(str(n))
    for i in range(tem):
        d=i%10
        sum=sum+d**tem
        i=i//10
    if sum==n:
        print("arm",n)
