'''WAP a program to desing the given program .

6 5 4 3 2 1
  6 5 4 3 2
    6 5 4 3
      6 5 4
        6 5
'''


n=int(input("="))
i=1
while i<=n:
    print()
    k=1
    while k<i:
        print(" ",end=" ")
        k=k+1
    j=n+1
    while j>=i:
        print(j,end=" ")
        j=j-1
    i=i+1