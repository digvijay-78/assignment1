'''WAP a program to desing the given program .
a
a b
a b c
a b c d
a b c d e'''




n=int(input("="))
c=97
for i in range(1,n+1):
	print("")
	for j in range(1,i+1):
		x=chr(c+j-1)
		print(x,end=" ")
