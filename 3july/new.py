'''WAP a program to desing the given program .
5 4 3 2 1
 5 4 3 2
  5 4 3
   5 4'''
n=int(input("="))
i=1
while i<=n:
    print()
    x=1
    while x<i:
        print("",end=" ")
        x=x+1
    k=n+1
    while k>=i:
        print(k,end=" ")
        k=k-1
    i=i+1
