'''
========================================
Assignment 1: Time Converter
========================================

An event management company is developing a scheduling system. One of the key tasks is converting the duration of events from total seconds (which their sensor system records) into a more human-readable format of hours, minutes, and seconds.

Write a Python program that:
- Accepts the total event duration in seconds as input.
- Calculates how many hours, minutes, and seconds it corresponds to.
- Displays the output in the format:
  Hours: x, Minutes: y, Seconds: z

Sample Input:
Total event duration in seconds: 3672

Sample Output:
Hours: 1, Minutes: 1, Seconds: 12
'''

duration=int(input("total event duration  in seconds:"))
hours=duration//3600
rem= duration%3600
min=rem//60
sec=rem%60
print("Hours:{},Min:{},Sec:{}".format(hours,min,sec))

'''
========================================
Assignment 2: Lifetime Calculator
========================================

You are developing a feature for a health and wellness mobile app that helps users understand how long they've been alive in a more tangible way.

Write a Python program that:
- Accepts the user’s age in years as input.
- Calculates the approximate number of:
  Days lived (1 year = 365 days)
  Hours lived
  Minutes lived
- Displays the output in the format:

You've lived approximately:
Days: xxx
Hours: yyy
Minutes: zzz

Sample Input:
Enter your age in years: 18

Sample Output:
You've lived approximately:
Days: 6570
Hours: 157680
Minutes: 9460800
'''
age=int(input("Enter your age in years:"))
days=age * 365+ age//4
print(days)
hours=age*365*24
print(hours)
min=age*365*24*60 
print(min)
'''
========================================
Assignment 3: Split the Bill
========================================

You and your friends went out to eat. The bill was quite high and you want to split it evenly.

Write a Python program that:
- Accepts the total bill amount.
- Accepts the number of friends.
- Displays how much each person should pay.

Example:
Total bill = 1250
Friends = 5
Each should pay = 250.0
'''

bill=float(input("Enter the total bill:"))
split=float(input("Enter the no. of friends:"))
each=bill/split
print("Total bill={}\nFriend={}\nEach should pay ={}".format(bill,split,each))

'''

========================================
Assignment 4: Travel Fare Calculator
========================================

A cab company charges ₹15 per kilometer.

Write a Python program that:
- Accepts the number of kilometers traveled.
- Calculates the total fare.
- Displays the result.

Example:
Distance = 20 km
Total fare = ₹300
'''
km=int(input("total kilometers traveled:"))
cal=km*15
print(f"Distance={km}km\nTotal fare=₹{cal}")
'''
========================================
Assignment 5: Shopping Tax Calculator
========================================

Your shopping cart total doesn’t include tax. A 12% GST is applied.

Write a Python program that:
- Accepts the cart total amount.
- Calculates 12% tax.
- Displays the tax and final total amount.

Example:
Cart = ₹2000
Tax = ₹240
Total = ₹2240
'''
'''
cart=float(input("Enter the total amount"))
tax=cart*(12/100)
total=cart+tax
print("Cart=₹{}\nTax=₹{}\nTotal=₹{}".format(cart,tax,total))'''
'''
========================================
Assignment 6: Smart Coin Machine
========================================

You insert an amount into a vending machine. It returns coins using the largest denominations possible (₹10 and ₹5).

Write a Python program that:
- Accepts the total amount.
- Calculates how many ₹10 coins and ₹5 coins will be dispensed.
- Displays the result.

Example:
Amount = ₹35
Output = ₹10 x 3, ₹5 x 1
'''

ammo=int(input("Enter the amount"))
ten=ammo//10
rem=ammo%10
five=rem//5

print("₹10 x {}, ₹5 x {}".format(ten,five))

'''

========================================
Assignment 7: Temperature Converter
========================================

A weather application needs to convert temperature from Celsius to Fahrenheit.

Write a Python program that:
- Accepts temperature in Celsius as input.
- Converts it to Fahrenheit using the formula:
  F = (C × 9/5) + 32
- Displays the result.

Example:
Celsius = 25
Fahrenheit = 77.0'''

cel =float(input("temperature in Celsius"))
far=(cel*9/5)+32
fari=float(far)
print(f"Celsius = {cel}\nFahrenheit = {fari}")

'''
========================================
Assignment 8: Simple Interest Calculator
========================================

A bank wants to help customers calculate the simple interest on their savings.

Write a Python program that:
- Accepts principal amount, rate of interest, and time (in years) as input.
- Calculates the simple interest using the formula:
  SI = (P × R × T) / 100
- Displays the simple interest.

Example:
Principal = 1000
Rate = 5
Time = 2
Simple Interest = 100.0
'''
p,r,t=map(float,input("Enter the principal amount, rate of interest, and time (in years) seperate them by space:").split())
si=(p*r*t)/100
print("Principal ={}\nRate = {}\nTime = {}\nSimple Interest = {}".format(p,r,t,si))
