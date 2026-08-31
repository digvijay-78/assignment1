'''3.
# Assignment: Prime Number Analyzer using List (Python)

## Scenario

A coaching institute stores student lucky numbers in a Python List.
Your task is to analyze the list and identify prime numbers for a scholarship 
selection process.

You must iterate through every element of the list and perform prime number analysis.


# Requirements

Write a Python program to:

1. Store integer values in a List
2. Iterate through all elements of the List
3. Check whether each number is prime or not
4. Display all prime numbers
5. Count total prime numbers
6. Count total non-prime numbers
7. Find the largest prime number from the List
8. Store all prime numbers into another List
9. Sort the prime numbers in ascending order and display them

---

# Test Case 1

## Input

[2, 3, 4, 5, 6, 7, 8]

## Expected Output

Prime Numbers: 2 3 5 7
Prime Count: 4
Non-Prime Count: 3
Largest Prime Number: 7
Prime List: [2, 3, 5, 7]
Sorted Prime List: [2, 3, 5, 7]

---

# Test Case 2

## Input

[10, 11, 12, 13, 14, 15]

## Expected Output

Prime Numbers: 11 13
Prime Count: 2
Non-Prime Count: 4
Largest Prime Number: 13
Prime List: [11, 13]
Sorted Prime List: [11, 13]

---

# Test Case 3

## Input

[1, 2, 17, 19, 20, 25]

## Expected Output

Prime Numbers: 2 17 19
Prime Count: 3
Non-Prime Count: 3
Largest Prime Number: 19
Prime List: [2, 17, 19]
Sorted Prime List: [2, 17, 19]

---

# Test Case 4

## Input

[4, 6, 8, 9, 10]

## Expected Output

Prime Numbers: None
Prime Count: 0
Non-Prime Count: 5
Largest Prime Number: Not Available
Prime List: []
Sorted Prime List: []

---

# Test Case 5

## Input

[29, 31, 37, 41]

## Expected Output

Prime Numbers: 29 31 37 41
Prime Count: 4
Non-Prime Count: 0
Largest Prime Number: 41
Prime List: [29, 31, 37, 41]
Sorted Prime List: [29, 31, 37, 41]

---'''
import math
n=list(map(int,input("enter the list").split()))
primeno=""
prime=[]
count=0

for i in n:
    if i<2:
        continue
    isprime=1
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            isprime=0
            break
    if isprime==1:
            primeno+=str(i)+" "
            count+=1
            prime.append(i)
if count>0:
    print(" Prime Numbers:",primeno)
else:
    print("Prime Numbers:none")
print("Prime Count:",count)
nonp=len(n)-count
print("Non-Prime Count:", nonp)

# if count > 0:
#     print("Largest Prime Number:", max(prime))
# else:
#     print("Largest Prime Number: Not Available")
if count>=1:
    a=prime[0]
    for k in prime:
        if a<k:
            a=k
    print("Largest Prime Number:", a)
else:
    print("Largest Prime Number: Not Available")

print("Prime List:", prime)
prime.sort()
print("Sorted Prime List:", prime)