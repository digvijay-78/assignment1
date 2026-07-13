'''
Q51  
55555
4444
333
22
1       

n=int(input("="))
for i in range(n,0,-1):
    for j in range(n-i):
       print(" ",end="")
    for k in range(i,0,-1):
       print(i,end="")
    print()

    
	
	
	
Q52
12345
 1__4
  1_3
   12
    1
	

n=int(input("="))
for i in range(n,0,-1):
    for k in range(1,(n-(i-1))):
       print(" ",end="")
    for j in range(1,i+1):
      if i==j or i==n or j==1:
         print(j,end="")
      else:
         print("_",end="")
    print()





Q53
55555
 4__4
  3_3
   22
    1

   	
n=int(input("="))
for i in range(n,0,-1):
    for k in range(1,(n-(i-1))):
       print(" ",end="")
    for j in range(1,i+1):
      if i==j or i==n or j==1:
         print(i,end="")
      else:
         print("_",end="")
    print()	
	

    
    
    
    
    
    
  
Q54    
ABCDE
 A__D
  A_C
   AB
    A
   
   
n=int(input("="))
for i in range(n,0,-1):
    for k in range(1,(n-(i-1))):
       print(" ",end="")
    for j in range(1,i+1):
      if i==j or i==n or j==1:
         print(chr(j+64),end="")
      else:
         print("_",end="")
    print()

    
    
    
    
Q55    
ABCDE
ABCD
ABC
AB
A

n=int(input("="))
for i in range(n,0,-1):
    for k in range(1,(n-(i-1))):
       print(" ",end="")
    for j in range(1,i+1):
         print(chr(j+64),end="")
    print()

    
    
    
Q56   
11111
 2222
  333
   44
    5
    
n=int(input("="))
for i in range(1,n+1):
    for k in range(1,i):
       print(" ",end="")
    for j in range(n,i-1,-1):
         print(i,end="")
    print()




Q57
    *
   * *
  * * *
 * * * *
* * * * *



n=int(input("="))
for i in range(1,n+1):
    for k in range(n,i,-1):
       print(" ",end="")
    for j in range(1,i+1):
                    print("*",end=" ")
    print()

    
Q58
    1 
   1 2 
  1 2 3 
 1 2 3 4 
1 2 3 4 5     

n=int(input("="))
for i in range(1,n+1):
    for k in range(n,i,-1):
       print(" ",end="")
    for j in range(1,i+1):
                    print(j,end=" ")
    print()






Q59
    
    A
   A B
  A B C
 A B C D
A B C D E


n=int(input("="))
for i in range(1,n+1):
    ch=65
    for j in range(n,i,-1):
       print(" ",end="")
    for j in range(1,i+1):
                    print(chr(ch),end=" ")
                    ch=ch+1
    print()

    





Q60
    X
   X X
  X__X
 X____X
X X X X X

n=int(input("="))
for i in range(1,n+1):
    for k in range(n,i,-1):
       print(" ",end="")
    for j in range(1,i+1):
      if j==1 or i==n or i==j:  
                    print("X",end=" ")
      else:
            print("_",end=" ")
    print()

    




Q61
    *
   ***
  *****
 *******
*********


n=int(input("="))
for i in range(1,n+1):
	for k in range(n,i,-1):
		print(" ",end="")
	for j in range(1,2*i):
		print("*" ,end="")
	print()
	




Q62
    1
   123
  12345
 1234567
123456789

n=int(input("="))
for i in range(1,n+1):
	for k in range(n,i,-1):
		print(" ",end="")
	for j in range(1,2*i):
		print(j ,end="")
	print()

    



Q63
    A
   ABC
  ABCDE
 ABCDEFG
ABCDEFGHI

n=int(input("="))
for i in range(1,n+1):
	for k in range(n,i,-1):
		print(" ",end="")
	for j in range(1,2*i):
		print(chr(j+64) ,end="")
	print()
    



Q64
    *
   *_*
  *___*
 *_____*
*********

n=int(input("="))
for i in range(1,n+1):
    for k in range(n-i,0,-1):
       print(" ",end="")
    for j in range(1,2*i):
      if j==1 or i==n or j==2*i-1  :  
                    print("*",end="")
      else:
            print("_",end="")
    print()
   






Q66
    1
   1_1
  1___1
 1_____1
111111111

n=int(input("="))
for i in range(1,n+1):
    for k in range(n-i,0,-1):
       print(" ",end="")
    for j in range(1,2*i):
      if j==1 or i==n or j==2*i-1  :  
                    print(1,end="")
      else:
            print("_",end="")
    print()


    
    
Q67    
     A
   B_B
  C___C
 D_____D
EEEEEEEEE
n=int(input("="))
for i in range(1,n+1):
    for k in range(n-i,0,-1):
       print(" ",end="")
    for j in range(1,2*i):
      if j==1 or i==n or j==2*i-1  :  
                    print(chr(i+64),end="")
      else:
            print("_",end="")
    print()


    
Q68
    #
   *#*
  **#**
 ***#***
****#****    

n = int(input("Enter n: "))

for i in range(1, n + 1):
    print()
    for k in range(n, i, -1):
        print(" ", end="")
    for j in range(1, 2 * i):
        if j == i:
            print("#", end="")
        else:
            print("*", end="")


Q69
*********
 *******
  *****
   ***
    *

n=int(input("="))
for i in range(n,0,-1):
	for k in range(n-i,0,-1):
		print(" ",end="")
	for j in range(1,2*i):
		print("*" ,end="")
	print()
	
    


Q70
* * * * * 
 * * * * 
  * * * 
   * * 
    * 

n=int(input("="))
for i in range(n,0,-1):
    for k in range(n-i,0,-1):
       print(" ",end="")
    for j in range(1,i+1):
                    print("*",end=" ")
    print()








Q71
123456789
 1234567
  12345
   123
    1

n=int(input("="))
for i in range(n,0,-1):
	for k in range(n-i,0,-1):
		print(" ",end="")
	for j in range(1,2*i):
		print(j ,end="")
	print()
	






Q72
A B C D E 
 A B C D 
  A B C 
   A B 
    A 

n=int(input("="))
for i in range(n,0,-1):
    ch=65
    for j in range(n-i,0,-1):
       print(" ",end="")
    for j in range(1,i+1):
                    print(chr(ch),end=" ")
                    ch=ch+1
    print()







Q73
5 5 5 5 5 
 4 4 4 4 
  3 3 3 
   2 2 
    1 

n=int(input("="))
for i in range(n,0,-1):
    for k in range(n-i,0,-1):
       print(" ",end="")
    for j in range(1,i+1):
                    print(i,end=" ")
    print()


    




    
123456789
 1_____7
  1___5
   1_3
    1    

n=int(input("="))
for i in range(n,0,-1):
   print()
   for k in range(n-i,0,-1):
     print(" ",end="")
   for j in range(1,2*i):
         if j==1 or i==n or j==2*i-1:
                 print(j ,end="")
         else:
            print(" ",end="")




123456789
 1+++++7
  1+++5
   1+3
    1

n=int(input("="))
for i in range(n,0,-1):
   print()
   for k in range(n-i,0,-1):
     print(" ",end="")
   for j in range(1,2*i):
         if j==1 or i==n or j==2*i-1:
                 print(j ,end="")
         else:
            print("+",end="")    

            
            
            
            
            
x
xx   
xxx
xxxx
xxxxx
xxxx
xxx
xx
x   

n=int(input("="))
for i in range(1,n+1):
	print()
	for j in range(1,i+1):
		print("x",end="")

for k in range(n,1,-1):
	print()
	for m in range(1,k):
	   print("x",end="")


Q
1
12
123
1234
123
12
1 

n=int(input("="))
for i in range(1,n+1):
	print()
	for j in range(1,i+1):
		print(j ,end="")

for k in range(n,1,-1):
	print()
	for m in range(1,k):
	   print(m,end="")
	   






Q
   1
  12
 123
1234
 123
  12
   1




n=int(input("="))
for i in range(1,n+1):
    for j in range(1,n-i+1):
       print(" ",end="")
    for k in range(1,i+1):
       print(k,end="")
    print()

for i in range(n,1,-1):
    for j in range(1,n+1-i+1):
       print(" ",end="")
    for k in range(1,i):
       print(k,end="")
    print()
	
	
	
	
	
1 
1 2 
1   3 
1     4 
1   3 
1 2 
1 

n=int(input("="))
for i in range(1,n+1):
	print()
	for j in range(1,i+1):
		if  j==1 or j==i:
			print(j,end=" ")
		else:
			print(" ",end=" ")
for i in range(n-1,0,-1):
	print()
	for k in range(1,i+1):
		if  k==1 or k==i:
			print(k,end=" ")
		else:
			print(" ",end=" ")
            

'''