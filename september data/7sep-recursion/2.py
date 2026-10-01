"""Assignment 2: Binary Converter for Embedded System

An embedded systems company develops microcontrollers that understand only binary values. Engineers enter decimal numbers, and the software must convert them into binary before sending them to the device.

As a software developer, write a recursive program to perform this conversion.

Task

Write a recursive function to convert a decimal number into its binary representation.

Input
Enter a decimal number:
25
Output
Binary Number = 11001

Note: Do not use Python's built-in bin() function."""

def binary(n):
    if n==1:
        return n
    binary(n//2)
    print(n%2, end= "")
    
n = int(input("enteer the number: "))
print(1, end ="")
binary(n)