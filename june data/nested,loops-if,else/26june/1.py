'''1. E-Learning Course Access System

An online learning platform grants access based on subscription type, course progress, and test score.

If subscription is premium, then check progress. If progress is at least 80, then check test score. If score is at least 70, unlock certificate; otherwise allow retry. If progress is less than 80, ask to complete course. If subscription is basic, then check progress. If progress is at least 50, allow limited access; otherwise lock content. If subscription is neither, deny access.

Input:
Subscription = premium
Progress = 85
Test Score = 65

Output:
Access Status = Retry Test'''

a=input("=")
b=int(input("="))
c=int(input("="))
if a.lower()=="premium":
	if b>=80:
		if c>=70:
			print(" unlock certificate")
		else:
			print("allow retry")
	else:
		if b<80:
			print("complete the course")
elif a.lower=="basic":
	if b>=50:
		print("allow limited access")
	else:
		if b<50:
			print("lock content")
else:
	print(" access denied")
			