'''2.
Fibonacci Series Generator

A learning app helps students understand number patterns. One of the most important patterns is the Fibonacci series, where each number is the sum of the previous two numbers.

The series starts with:
0 1

Write a program to:

- Read a number n (number of terms)
- Print the Fibonacci series up to n terms using a loop

Input:
7

Output:
0 1 1 2 3 5 8
'''
n=int(input("enter"))
a=0
b=1
sum=0
for i in range(n-1):
	print(sum,end=" ")
	sum=a+b
	a=b
	b=sum
	