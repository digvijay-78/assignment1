2. Multi Stage Prime Lock System


A smart locker opens only if final derived number is prime.


Write a program to:


- Find sum of digits

- Find product of digits

- Find difference between product and sum

- Count digits in difference

- Add digit count to difference

- Check whether final result is Prime or Not


Input:

234


Output:

Sum = 9

Product = 24

Difference = 15

Digits = 2

Final Result = 17

Prime
n=int(input("="))
sum=n
sum1=0
for i in range(len(str(n))):
    d=sum%10
    sum1=sum1+d
    sum=sum//10
pro=n
pro1=1
for i in range(len(str(n))):
    d=sum%10
    pro1=pro*d
    pro=pro//10
diff=abs(pro1-sum1)
count=0
for d in range(len(str(diff))):
	d=diff%10
	count=count+1
	diff=diff//10
final=diff+count
if final<=1:
	print("not")
else:
	for i in range(2,final//2):
		if final%i==0:
			print("not a prime")
			break
	else:
		print("prime no.")