'''3. Banking Fraud Detection System

A bank monitors transactions based on amount, location, OTP verification, and account age.

If transaction amount is at least 10000, then check location. If international, then check OTP verification. If verified, allow; otherwise block. If location is domestic, then check if amount is at least 50000. If yes, check account age. If account age is at least 2 years, allow; otherwise flag. If amount is less than 50000, allow. If transaction amount is less than 10000, then check unusual activity. If yes, flag; otherwise allow.

Input:
Transaction Amount = 60000
Location = domestic
Account Age = 1

Output:
Transaction Status = Flagged
'''
amount=int(input("="))
location =input("=")

if amount >=10000:
	if location.lower()=="international":
		otp=input("OTP Verified (yes/no) = ")
		
		if otp.lower()=="yes":
			print("Transaction Status = OTP verified")
		else:
			print("Transaction Status = blocked")

	elif location.lower()=="domestic":
		if amount>=50000:
			age=int(input("account age="))
			if age>=2:
				print("Transaction Status = allowed")
			else:
				print("Transaction Status = flagged")
		else:
			print("Transaction Status = allowed")
else:
     unusual = input("Unusual Activity (yes/no) = ")
     if unusual.lower()=="yes":
             print("Transaction Status = Flagged")	
     else:
             print("Transaction Status = Allowed")