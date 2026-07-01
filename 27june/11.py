'''n=int(input("="))
sum=n**2
for i in range (len(str(n))):
	d=sum%10	
	i=n%10
	
if i==d:
	print("automorphic")
else:
	print("not")
n=int(input("="))
sum=n**2
for i in range (len(str(n))):
	d=sum%10	
	i=n%10
	sum=sum//10
	n=n//10
	if i!=d:
		print("not automorphic")
	break
else:
	print("automorphic")'''



n=input("=")
m=n
for i in range n:
	i=n//10
	if i==0:
		print("rejected")	
	break
	else:
		i=i%10
		if i==0:
			print("duck")
		n=n//10

		