'''import math
n=int(input("enter the no"))
print(math.factorial(n))



n=int(input(""))
sum=0
i=1
while i<=n//2:
	if n%i==0:
		sum+=i
	i+=1
if sum==n:
	print("p")
else:
	print("v")


for i in range (1,21):
	if i%2==0:
		continue
	print(i)



a=[10,20,30]
b=[10,20,30]
print(a is not b)
print(a is b)
print(a ==b)


print(5|6)
print(5^6)
print(5&6)



s="Leetcode"
lower=0
uper=0
for i in s:
	if "a"<=i<="z":
		lower+=1
	else:
		uper+=1
if "A"<=s[0]<="Z":
	lower+=1
if len(s)==lower or len(s)==uper:
	print(True)
else:
	print(False)
'''


