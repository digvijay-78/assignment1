#patterns 
'''
WAP to print the pattern


q1
*****
n=int(input("="))
for i in range(n):
	print("*",end=" ")





Q2
*
*
*
*
*
n=int(input("="))
for i in range(n):
	print("*")




Q3

*
 *
  *
   *
    *
n=int(input("="))
for i in range(0,n):
	print(i*" ","*")

	

Q4
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




Q5
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


Q6
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


Q7
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



Q8

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


		

Q9
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





Q10
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




Q11
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





Q12
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



Q13
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




Q14
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




Q15
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
        
        
        
        
        

Q16        
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

        
        
        
Q17        
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






Q18
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

            
            
            
            
            
Q19
*
* *
*   *
*     *
* * * * *            

n=int(input("="))
for i in range(1,n+1):
	for j in range(1,i+1):
		if n==i or j==1 or j==i:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()




	


Q20	
1
12
1 3
1  4
12345

n=int(input("="))
for i in range(1,n+1):
	for j in range(1,i+1):
		if n==i or j==1 or j==i:
			print(j,end=" ")
		else:
			print(" ",end=" ")
	print()

      
      
      
      
      
      
Q21        
1
22
3 3
4  4
55555            

n=int(input("="))
for i in range(1,n+1):
	for j in range(1,i+1):
		if n==i or j==1 or j==i:
			print(i,end=" ")
		else:
			print(" ",end=" ")
	print()

    
Q22    
A
AB
A C
A  D
ABCDE    


n=int(input("="))
for i in range(1,n+1):
	ch=65
	for j in range(1,i+1):
		if n==i or j==1 or j==i:
			print(chr(ch),end=" ")
		else:
			print(" ",end=" ")
		ch=ch+1
	print()

      
      
      
Q23      
a
bc
d f
g  j
klmno

n=int(input("="))
ch=97
for i in range(1,n+1):
	for j in range(1,i+1):
		if n==i or j==1 or j==i:
			print(chr(ch),end=" ")
		else:
			print(" ",end=" ")
		ch=ch+1
	print()

      
      
      
      
Q24      
*
**
*@*
*@@*
* * * * *
   

n=int(input("="))
for i in range(1,n+1):
	for j in range(1,i+1):
		if n==i or j==1 or j==i:
			print("*",end=" ")
		else:
			print("@",end=" ")
	print()



Q25    
5
54
543
5432
54321


     
n=int(input("="))
for i in range(n+1,0,-1):
	for j in range(n,i-1,-1):
		print(j ,end=" ")
	print()    



Q26
*
*#
*#*
*#*#
*#*#*  


n=int(input("="))
for i in range(1,n+1):
    print()
    for j in range(1,i+1):
        if j%2==0:
            print("#",end=" ")
        else:
            print("*",end=" ")
            

            
            
            
            
Q27            
1
10
1 1
1  0
10101            
        
n=int(input("="))
for i in range(1,n+1):
    for j in range(1,i+1):
        if n==i or j==1 or j==i:
                if j%2==0:
                        print(0,end=" ")
                else:
                      print(1,end=" ")
        else:
              print(" ",end=" ")
    print()

Q28
1
123
12345
1234567
123456789

n=int(input("="))
for i in range(1,n+1):
	print()
	for j in range(1,2*i):
		print(j ,end=" ")

            
                  
Q29                       
1
222
33333
4444444
555555555
                                      

n=int(input("="))
for i in range(1,n+1):
	print()
	for j in range(1,2*i):
		print(i ,end=" ")
                

        
        
        
        
        
Q30             
*****
****
***
**
*             
                
                
                
     
n=int(input("="))
for i in range(1,n+1):
    print()
    for j in range(n,i-1,-1):
        print("*",end=" ")       

        
        
Q31        
12345
1234
123
12
1             
        
n=int(input("="))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()






Q32    
55555
4444
333
22
1      

n=int(input("="))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(i,end=" ")
    print()


	


Q33
ABCDE
ABCD
ABC
AB
A


n=int(input("="))
for i in range(n,0,-1):
    ch=65
    for j in range(1,i+1):
        print(chr(ch),end=" ")
        ch=ch+1
    print()




Q34
EEEEE
DDDD
CCC
BB
A
   
n=int(input("="))
for i in range(n,0,-1):
    ch=65+i-1
    for j in range(i):
        print(chr(ch),end=" ")
    print()

    
    
    
Q35    
*****
*  *
* *
**
*



n=int(input("="))
for i in range(n,0,-1):
	for j in range(1,i+1):
		if n==i or j==1 or j==i:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()

    
    
    
    
Q36   
ABCDE
A  D
A C
AB
A    

n=int(input("="))
for i in range(n,0,-1):
	ch=65
	for j in range(1,i+1):
		if n==i or j==1 or j==i:
			print(chr(ch),end=" ")
		else:
			print(" ",end=" ")
		ch=ch+1
	print()

q37  
*****
####
***
##
*
        

n=int(input("="))
for i in range(n+1,1,-1):
	print()
	for j in range(i,1,-1):
		if i%2==0:
			print("*",end=" ")
		else:
			print("#",end=" ")

            
            
            
            
            
            
            
Q38           
55555
4  4
3 3
22
1            

 
n=int(input("="))
for i in range(n,0,-1):
	for j in range(1,i+1):
		if n==i or j==1 or j==i:
			print(i,end=" ")
		else:
			print(" ",end=" ")
	print()           
            
                    
Q39           
123456
54321
1234
321
12
1         

n=int(input("="))
for i in range(n,0,-1):
		if i%2!=0:
			for k in range(i,0,-1):
				print(k ,end=" ")
		else:
			for n in range(1,i+1):
				print(n,end=" ")
		print()

		
		
		
		
		
Q40		
*
**
****
*******
**********
		

n=int(input("="))
for i in range(1,n+1):
	print()
	for j in range(1,2*i):
		print(j ,end=" ")



Q41
A
BCD
EFGHI
JKLMNOP


n=int(input("="))
ch=65
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(ch),end=" ")
        ch=ch+1
    print()





       
Q42    
54321
5432
543
54
5
        
n=int(input("="))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

    
    
    
    
    
    
    
    
Q43    
	1
   12
  123
 1234
12345


n=int(input("="))
for i in range(1,n+1):
    for j in range(1,n-i):
       print(" ",end="")
    for k in range(1,i+1):
       print(k,end="")
    print()

    
    
    
 Q44   
    1
   22
  333
 4444
55555
    


n=int(input("="))
for i in range(1,n+1):
    for j in range(n+1,i,-1):
       print(" ",end="")
    for k in range(i,0,-1):
       print(i,end="")
    print()
    
    
    
    
Q45
    
    5
   44
  333
 2222
11111


n=int(input("="))
for i in range(n,0,-1):
    for j in range(i,n-i,-1):
       print(" ",end="")
    for k in range(n,i-1,-1):
       print(i,end="")
    print()
        

    
Q46 
    A
   AB
  ABC
 ABCD
ABCDE

n=int(input("="))
for i in range(1,n+1):
    ch=65
    for j in range(1,n-i):
       print(" ",end="")
    for k in range(1,i+1):
       print(chr(ch),end="")
       ch=ch+1
    print()
    


Q47
    1
   11
  1*1
 1**1
11111

n=int(input("="))
for i in range(1,n+1):
	for j in range(1,i+1):
		if n==i or j==1 or j==i:
			print(1,end=" ")
		else:
			print("*",end=" ")
	print()


    
    
    
    
    
Q48    
A
AB
A_C
A__D
ABCDE
    
n=int(input("="))
for i in range(1,n+1):
	print()
	for s in range(n,i-1,-1):
					print(" ",end="")
	for j in range(1,i+1):
            if n==i or j==1 or j==i:
                    print(chr(j+64),end="")
            else:
                    print("_",end="")
                    
                    
                    
                    

                    
                    
                    
Q49
	1
   10
  101
 1010
10101

n=int(input("="))
for i in range(1,n+1):
    print()
    for s in range(n,i-1,-1):
          print(" ",end=" ")
    for j in range(1,i+1):
        if j%2==0:
            print(0,end=" ")
        else:
            print(1,end=" ")

            
            
            
            
            
                        
Q50
12345
 1234
  123
   12
    1

n=int(input("="))
for i in range(n,0,-1):
    for j in range(1,n-i+1):
       print(" ",end="")
    for k in range(1,i+1):
       print(k,end="")
    print()
    
    
    
'''   

n=int(input("="))
for i in range(n,0,-1):
		if i%2!=0:
			for k in range(i,0,-1):
				print(k ,end="")
		else:
			for n in range(1,i+1):
				print(n,end="")
		print()