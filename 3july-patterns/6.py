'''WAP a program to desing the given program .
'''
n=int(input("Enter number of lines"))

for i in range(1,n+1):
    for j in range(n+1,i,-1):
       print(" ",end="")
    for k in range(i,0,-1):
        if (k+i)%2==0:
            print(1,end="")
        else:
            print(0,end="")
    print()
