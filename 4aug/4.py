'''4.
Palindrome Number List Checker
Scenario
A system checks lucky numbers which are palindromes.
Requirements
Check palindrome numbers
Store palindrome numbers in list
Count palindrome numbers
Find largest palindrome
Sort palindrome list
Test Cases
Input:
[121, 131, 20, 44, 55, 100]

Output:

Palindromes: [121, 131, 44, 55]
Count: 4
Largest: 131
Sorted: [44, 55, 121, 131]'''

a=list(map(int,input("enter list").split()))
l=[]
for i in a :
    if str(i)==str(i)[::-1]:
            l.append(i)
print("Palindromes:",l)
print("Count:", len(l))
if  len(l)> 0:
    print("Largest Prime Number:", max(l))
else:
    print("Largest Prime Number: Not Available")
l.sort()
print("Sorted Prime List:", l)