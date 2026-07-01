'''7.

 Alternate Digit Prime Checker


A math lab adds alternate digits from right side.


Write a program to:


- Find sum of alternate digits

- Check whether sum is Prime or Not


Input:

12345


Output:

Alternate Sum = 9

Not Prime
'''

n=int(input("="))
sum=0
for i in range (len(str(n))):
    d=n%10
    n=n//10
    if i%2==0:
        print(d)
        sum=sum+d
print("alternate",sum)
if sum<=1:
    print("not a prime no.")
else:
    for i in range(2,sum//2):
        if sum%i==0:
            print("not")
            break
    else:
        print("prime no")    