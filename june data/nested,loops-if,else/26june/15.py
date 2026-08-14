'''15. E-Commerce Dynamic Pricing System

An e-commerce system gives discount based on demand, stock, user type, and festival.

If demand is 80 or above, then check stock. If stock is less than 50, then check user type. If user is premium, then check festival. If festival is yes, give 20% discount; otherwise 10%. If user is not premium, no discount. If stock is 50 or more, give 5% discount.

If demand is between 40 and 79, then check festival. If yes, give 10% discount; otherwise no discount.

If demand is below 40, then check stock. If stock is greater than 200, give 15% discount; otherwise no discount.

Input:
Demand = 85
Stock = 40
User Type = premium
Festival = yes

Output:
Discount = 20%
'''
demand=int(input("="))
stock=int(input("="))
type =input("=")
festival=input("=")

if demand >=80:
	if stock<50:
		if type.lower()=="premium":
			if festival.lower()=="yes":
			print("Discount = 20%")
			else:
			print("Discount = 10%")
		else:
			print("no Discount")
	else:
		if stock>=50:
				print("Discount = 5%")

elif demand >=40:
	if festival.lower()=="yes":
		print("Discount = 10%")
	else:
		print("no Discount ")

else:
	if stock>=200:
		print("Discount = 20%")
	else:
		print("no Discount ")

	