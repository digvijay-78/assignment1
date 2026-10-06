'''Assignment 1: Speed Calculator

Write a Python program that:

Accepts distance (in km) and time (in hours).
Calculates speed.

Input:
Distance = 120
Time = 2

Output:
Speed = 60 km/h

cal1=int(input("Enter the distance and (in km):"))
cal2=int(input("Enter the time and (in h):"))
speed= cal1 //cal2
print("speed={}km/h".format(speed))
'''

'''
----------------------------------------
Assignment 2: Salary Calculator

Write a Python program that:

Accepts daily wage and number of days.
Calculates total salary.

Input:
Daily wage = 500
Days = 26

Output:
Salary = 13000


daily=int(input("Enter the daily wages):"))
days=int(input("Enter the no. of  days :"))
speed= cal1 *cal2
print("speed=",speed)
'''
'''
----------------------------------------------
Assignment 3: Electricity Bill Calculator

Write a Python program that:

Accepts number of units.
Calculates bill (₹6 per unit).

Input:
Units = 100

Output:
Bill = 600
unit=int(input("Enter the units:"))
bill=unit*6
print("Bill=",bill)

------------------------------------------
Assignment 4: Area of Rectangle

Write a Python program that:

Accepts length and breadth.
Calculates area.

Input:
Length = 10
Breadth = 5

Output:
Area = 50
'''
#cal,cal1=map(int,input("Enter the lenth and breadth :").split())
#area=cal*cal1
#print(area)
'''
------------------------------------------------
Assignment 5: Average Marks Calculator

Write a Python program that:

Accepts marks of 3 subjects.
Calculates average.

Input:
Marks = 80, 90, 70

Output:
Average = 80.0
'''
#cal,cal1,cal2=map(int,input("write 3 subject marks folowed by space :").split())
#avg=cal+cal1+cal2/3
#avg1=float(avg)
#print("Average=",avg1)
'''
------------------------------------------------------------
Assignment 6: Discount Calculator

Write a Python program that:

Accepts total amount.
Calculates 10% discount and final price.

Input:
Amount = 1000

Output:
Discount = 100
Final = 900'''
'''
amo=int(input("Enter the total Amount:"))
percentage=amo*10/100
final=amo-percentage
print("Discount={}\nFinal={}".format(percentage,final))'''
'''
----------------------------------------------------------------
Assignment 7: Circle Area Calculator

Write a Python program that:

Accepts radius.
Calculates area of circle.

Input:
Radius = 7

Output:
Area = 153.86'''

#cal=int(input("Enter the area of circle:"))
#area=3.14*cal*cal
#print(area)
'''
------------------------------------------------------------------------
Assignment 8: Data Storage Converter

Write a Python program that:

Accepts value in MB.
Converts into GB.

Input:
MB = 2048

Output:
GB = 2.0
----------------------------------------------------------------------
'''
#cal1=int(input("Enter values in MB:"))
#gb=cal1/1024
#print(gb)
'''
Assignment 9: Fuel Cost Calculator

Write a Python program that:

Accepts distance (km), mileage (km/litre), and petrol price.
Calculates total fuel cost.

Input:
Distance = 100
Mileage = 20
Petrol Price = 100

Output:
Cost = 500
'''
'''
dis=int(input("Enter the distance and (in km):"))
mil=int(input("Enter the Milage (in km/l):"))
petrol=int(input("Enter the Petrol price:"))
price=dis//mil*petrol
print(price)'''
'''
Assignment 10: Percentage Calculator

Write a Python program that:

Accepts total marks and obtained marks.
Calculates percentage.

Input:
Total = 500
Obtained = 400

Output:
Percentage = 80%
'''
'''
tmark=int(input("Enter the total marks"))
omark=int(input("Enter the marks obtained"))
per= tmark/omark*100
print(per)'''
'''

Assignment 11: Time Duration Adder

Write a Python program that:

Accepts hours, minutes, seconds.
Converts into total seconds.

Input:
Hours = 1
Minutes = 2
Seconds = 30

Output:
Total Seconds = 3750
'''
'''
r=int(input("Enter hours:"))h
min=int(input("Enter min:"))
sec=int(input("Enter sec:"))
total = (hr*3600)+min*60+sec
print(total)'''

'''

Assignment 12: Change Return System

Write a Python program that:

Accepts amount.
Calculates ₹100, ₹50, ₹10 notes.

Input:
Amount = 380

Output:
₹100 x 3
₹50 x 1
₹10 x 3
'''
'''
cal=int(input("Enter the amount:"))
hun=cal//100
hun1=cal%100
fifty=hun1//50
hun2=hun1%50
ten=hun2//10
print("{}\n{}\n{}".format(hun,fifty,ten))
'''
'''
Assignment 13: Compound Interest Calculator

Write a Python program that:

Accepts principal, rate, and time.
Calculates compound interest.

Input:
Principal = 1000
Rate = 10
Time = 2

Output:
Amount = 1210.0
Compound Interest = 210.0

'''
'''p,r,t=map(int,input("Enter the principal, rate ,time:").split())
forme=p*(1+r/100)**t
for12=forme-p
form=int(forme)
for1=int(for12)
print(f"amount={form}\ncp={for1}")
'''
'''

Assignment 14: Simple Profit or Loss Calculator

Write a Python program that:

Accepts cost price and selling price.
Calculates profit/loss and percentage.

Input:
Cost Price = 1000
Selling Price = 1200

Output:
Profit = 200
Profit % = 20.0
'''
'''a=int(input("Enter the cost price:"))
b=int(input("Enter the selling price:"))
profit=b-a
per=profit/a*100
print(per)
'''

'''

Assignment 15: Average Speed for Multiple Trips

Write a Python program that:

Accepts distance1, time1, distance2, time2.
Calculates average speed.

Input:
Distance1 = 60
Time1 = 1
Distance2 = 40
Time2 = 1

Output:
Average Speed = 50 km/h'''
a=int(input("Enter the distance 1:"))
b=int(input("Enter the time 1:"))
c=int(input("Enter the distance 2:"))
d=int(input("Enter the time 2:"))

formula= (a+c)/(b+d)
print(formula)
