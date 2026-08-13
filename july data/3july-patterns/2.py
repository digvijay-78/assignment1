'''WAP a program to desing the given program .
A
AB
ABC
ABCD
ABCDE'''
n=int(input("="))
c=65
for i in range(1,n+1):
	print("")
	for j in range(1,i+1):
		x=chr(c+j-1)
		print(x,end=" ")

