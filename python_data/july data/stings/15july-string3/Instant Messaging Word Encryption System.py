'''4.  Instant Messaging Word Encryption System

A messaging application wants to temporarily encrypt messages during
transmission. The encryption rule is to reverse every word individually
while keeping the word positions unchanged.

Input: Enter message: java is powerful

Output: Encrypted Message: avaj si lufrewop
'''
n=input("Enter message: ").split()
print("Encrypted message: ",end=" ")
for i in range(len(n)):
	a=n[i]
	b=a[::-1]
	print(b,end=" ")
	