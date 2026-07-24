'''6.

Product Code Verification System

An e-commerce company wants to verify whether two product codes are rearranged versions of each other.

Conditions:
- Ignore spaces
- Ignore case sensitivity

Input:
Enter first product code: Dormitory
Enter second product code: Dirty Room

Output:
Both Product Codes are Matching'''

# s1=input("enter the string").split()
# s2=input("enter the string").split()
# if len(s1)==len(s2):
#     if sorted(s1)==sorted(s2):
#         print("Both Product Codes are Matching")
#     else:
#         print("not matching")
# else:
#     print("not matching")



s1=input("=")
s2=input("=")
a=""
b=""
for i in s1:
    if i!=" ":
        a=a+i.lower()
for i in s2:
    if i!=" ":
        b=b+i.lower()

if len(a)==len(b):
    if sorted(a)==sorted(b):
        print("Both Product Codes are Matching")
    else:
        print("Not Matching")
else:
    print("Not Matching")