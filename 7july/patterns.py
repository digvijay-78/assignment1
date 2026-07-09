#patterns 
'''
WAP to print the pattern



*****
n=int(input("="))
for i in range(n):
	print("*",end=" ")






*
*
*
*
*
n=int(input("="))
for i in range(n):
	print("*")






*
 *
  *
   *
    *
n=int(input("="))
for i in range(0,n):
	print(i*" ","*")

	


*****
*****
*****
*****
*****
n=int(input("="))
for i in range(0,n):
	print()
	for j in range(1,n+1):
		print("*",end=" ")





12345
12345
12345
12345
12345

n=int(input("="))
for i in range(0,n):
	print()
	for j in range(1,n+1):
		print(j ,end=" ")



11111
22222
33333
44444
55555

n=int(input("="))
for i in range(1,n+1):
	print()
	for j in range(1,n+1):
		print(i ,end=" ")



1
00
111
0000
11111

n=int(input("="))
for i in range(1,n+1):
	print()
	for j in range(1,i+1):
		if i%2==0:
			print(0 ,end=" ")
		else:
			print(1,end=" ")





*
**
***
****
*****

n=int(input("="))
for i in range(1,n+1):
	print()
	for j in range(1,i+1):
		print("*" ,end=" ")


1
22
333
4444
55555

n=int(input("="))
for i in range(1,n+1):
	print()
	for j in range(1,i+1):
		print(i ,end=" ")






1
12
123
1234
12345

n=int(input("="))
for i in range(1,n+1):
	print()
	for j in range(1,i+1):
		print(j ,end=" ")




A
AB
ABC
ABCD
ABCDE


n=int(input("="))
for i in range(1,n+1):
	print()
	ch=65
	for j in range(1,i+1):
		print(chr(ch) ,end=" ")
		ch=ch+1





a
ab
abc
abcd
abcde

n=int(input("="))
for i in range(1,n+1):
	print()
	ch=97
	for j in range(1,i+1):
		print(chr(ch) ,end=" ")
		ch=ch+1

1
01
101
0101
10101

n = int(input("="))
for i in range(1, n + 1):
    print()
    for j in range(1, i + 1):
        if i % 2 == 0:
            if j % 2 == 0:
                print(0, end=" ")
            else:
                print(1, end=" ")
        else:
            if j % 2 != 0:
                print(0, end=" ")
            else:
                print(1, end=" ")





1
23
456
78910

n=int(input("="))
k=1
for i in range(1,n+1):
	print()
	for j in range(1,i+1):
		print(k,end=" ")
		k+=1





A
BB
CCC
DDDD
EEEEE

n=int(input("="))
for i in range(1,n+1):
	print()
	ch=65
	a=chr(ch)
	for x in range(1,i):
		ch+=1
	for k in range(1,i+1):
		print(chr(ch),end=" ")
        
        
        
        
        

        
a
bc
def
ghij
klmno


n=int(input("="))
k=97
for i in range(1,n+1):
	print()
	for j in range(1,i+1):
		print(chr(k),end=" ")
		k+=1

        
        
        
        
*
##
***
####
*****        

n=int(input("="))
for i in range(1,n+1):
	print()
	for j in range(1,i+1):
		if i%2==0:
			print("#" ,end=" ")
		else:
			print("*",end=" ")







1
10
101
1010
10101

n=int(input("="))
for i in range(1,n+1):
    print()
    for j in range(1,i+1):
        if j%2==0:
            print(0,end=" ")
        else:
            print(1,end=" ")

            
            
            
            
            

*
* *
*  *
*   *
* * * * *            
'''
n=int(input("="))
for i in range(1,n+1):
	print()
	for k in range(1,i+1):
		s=n-i
		print(" "*s,end=" ")
	for j in range(1,i+1):
		print(j ,end=" ")




