'''WAP a program to desing the given program 
100-200
if divisible by 9 plus it.'''

n=int(input("="))
m=int(input("="))
sum=0
for i in range(n,m+1):
    if i%9==0:
        sum=sum+i
print(sum)