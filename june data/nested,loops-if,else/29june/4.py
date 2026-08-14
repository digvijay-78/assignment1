'''4. Prime Security Code Checker – Advanced

A high-security lab accepts only prime numbered access codes.

When a user enters a number, the software must:

- Check whether number is prime
- If prime, print next immediate prime number
- If not prime, print previous immediate prime number

Write a program using loops only.

Input:
29

Output:
Prime Number
Next Prime = 31
'''
n=int(input("="))

#prime no
if n<2:
	for i in range(2,n):
		if n%i==0:
			print("Not a prime no.")
			break 
	else:
		print("prime no hai sir")
#next prime
		m=n+1
		while True:
			for j in range(2,m):
				if m%j ==0:
					break
			else:
				print(m)
				break
			n+=1
#previous prime no
				p=n-1
			while p>1:
				for k in range(2,p):
					if p%k ==0:
						break
				else:
					print(p)
					break
				n-=1



