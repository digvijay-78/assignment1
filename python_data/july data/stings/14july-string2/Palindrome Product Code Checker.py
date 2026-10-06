'''5.
Palindrome Product Code Checker

A factory wants to identify whether a product code reads the same forward and backward.

Input:
Enter product code: MADAM

Output:
Palindrome Code

Input:
Enter product code: PRODUCT

Output:
Not a Palindrome Code'''
n=input("=")
a=n[::-1]
rev=""
for i in a:
	rev=rev+chr(ord(i))

#if n == n[::-1]:
#    print("Palindrome Code")
if rev==n:
	print("palindorme")
else:
	print("not a palindrome")