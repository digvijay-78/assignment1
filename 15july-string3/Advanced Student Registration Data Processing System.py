'''

6.
 Advanced Student Registration Data Processing System

A national university is developing an intelligent registration portal.
Students enter registration codes using uppercase letters, lowercase
letters, digits, and special symbols. Due to inconsistent data entry,
the administration wants the system to standardize and process the
information before storing it.

Conditions: - Ignore all special characters (@ # $ % & * - _) - Separate
alphabets and digits - Convert all alphabets to lowercase - Remove
duplicate alphabets - Arrange alphabets in ascending order - Arrange
digits in descending order - Display alphabets first and digits later -
If no digits are found, display “No Digits Found”

Test Case 1 Input: Enter registration code: zBc@638

Output: Result: bcz863

Test Case 2 Input: Enter registration code: 5Br$dE654b

Output: Result: bder6554

Test Case 3 Input: Enter registration code: A9@C3d#6B1a

Output: Result: abcd9631

Test Case 4 Input: Enter registration code: X#X@M2A4x7

Output: Result: amx742

Test Case 5 Input: Enter registration code: r@T#y

Output: Result: rty No Digits Found
'''
s = input("")
s1 = s2 = result = ""

for x in s:
    if x.isalpha():
        x = x.lower()
        if x not in s1:
            s1 = s1 + x
    elif x.isdigit():
        s2 = s2 + x

for x in sorted(s1):
    result = result + x

for i in range(len(sorted(s2))-1, -1, -1):
    result = result + s2[i]

print("Result:", result)

if s2 == "":
    print("No Digits Found")




# a = input("Enter the registration code: ").lower()
# alpha = ""
# digit= ""
# result= ""
# for i in range(len(a)):
    # if "a"<= a[i] <="z":
        # if a[i] not in alpha:
            # alpha = alpha + a[i]
    # elif "0"<=a[i]<="9":
            # digit = digit + a[i]
# 
# for j in range(97, 123):
    # for i in range(len(alpha)):
        # if alpha[i]==chr(j):
            # result = result + alpha[i]
# 
# k = 9
# while k>=0:
    # i = 0
    # while i<len(digit):
        # if digit[i] == str(k):
            # result = result + digit[i]
        # i+=1
    # k-=1
# 
# print(result)
# if digit== "":
    # print("No Digits Found.........")