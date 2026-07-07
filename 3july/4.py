'''WAP a program to desing the given program .
     *
    **
   ***
  ****
 *****
******'''
'''n=int(input("="))
i=1
while i<=n:
    x=n-1
    while x>=i:
        print(" ",end="")
        x-=1
    j=i
    while j>=1:
        print("*",end="") 
        j-=1
    print()   
    i+=1 '''


n=int(input("Enter number of lines"))

for i in range(1,n+1):
    for j in range(n+1,i,-1):
       print(" ",end="")
    for k in range(i,0,-1):
       print("*",end="")
    print()

