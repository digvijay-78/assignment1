'''
Note:

* Do NOT use if-else
* All percentages are given as whole numbers (like 5, 10). Convert using (value ÷ 100)
* Follow correct operator precedence and associativity
* Use ** for power (exponent), not ^

---

Assignment 1: Restaurant Bill Split

A group of friends went to a restaurant. The restaurant adds GST and service charge to the bill, and then the total is divided equally.

Input:
Total bill amount = 2500
GST = 5%
Service charge = 10%
Number of friends = 4

Expected Output:
Final Bill = 2875.0
Each Person Pays = 718.75

a,b,c,d=map(int,input("Enter the total bill ,GST,service,no of friends:" ).split())
bill =a+(b/100)*a+(c/100)*a
each=bill/d
print(bill)
print(each)

---

Assignment 2: Mobile EMI Calculation

You purchased a mobile phone using EMI. After paying a down payment, the remaining amount includes interest and is divided into monthly installments.

Input:
Mobile price = 30000
Down payment = 5000
Interest rate = 10%
Months = 10

Expected Output:
Remaining Amount = 25000
Total with Interest = 27500
Monthly EMI = 2750.0

a,b,c,d=map(int,input("Enter the mobile price ,downpay,rate,months " ).split())
rem=a-b
intrest=rem+(c/100)*rem
month=intrest/d
print("Remaining Amount ={}\nTotal with Interest = {}\nMonthly EMI = {}".format(rem,intrest,month))


---

Assignment 3: Student Marks Analysis

A student wants to calculate total marks, average, and percentage from 5 subjects.

Input:
Marks = 78, 85, 90, 88, 80

Expected Output:
Total = 421
Average = 84.2
Percentage = 84.2

a,b,c,d,e=map(int,input("Enter the marks seperated by ',' " ).split(","))
total=a+b+c+d+e
per_avg=total/5
print("total={}\navg={}\npercentage={}".format(total,per_avg,per_avg))
---

Assignment 4: Travel Distance Calculation

A person is traveling at a constant speed. Time is given in hours and minutes. Convert total time into hours and calculate distance.

Input:
Speed = 60 km/hr
Time = 2 hours 30 minutes

Expected Output:
Total Time = 2.5 hours
Distance = 150.0 km


a=float(input("enter the speed"))
b,c=map(float,input("Enter the time").split(","))
d=c/60
time=b+d
print(time)
distance=a*time
print(distance)


---

Assignment 5: Salary Breakdown

An employee wants to calculate salary per day and per hour.

Input:
Monthly salary = 36000
Working days = 24
Working hours per day = 8

Expected Output:
Salary per day = 1500.0
Salary per hour = 187.5

a,b,c=map(float,input("Enter the salary,days , hr").split(","))
day=a/b
hr=day/c
print(day)
print(hr)


---

Assignment 6: Data Storage Conversion

A user wants to convert data from GB into MB and KB.

Input:
Data = 5 GB

Expected Output:
In MB = 5120.0
In KB = 5242880.0


a=int(input("Enter the data (in GB):"))
mb=float(a*1024)
kb=float(mb*1024)
print(mb)
print(kb)

---

Assignment 7: Cricket Run Rate

In cricket, overs are given in decimal format (e.g., 48.3 means 48 overs and 3 balls). Convert overs into total balls and calculate run rate.

Input:
Total runs = 275
Overs = 48.3

Expected Output:
Total Balls = 291
Run Rate = 5.67
'''
'''
b,c=map(float,input("Enter the  runs and over").split(","))
no=int(c)
a=(c*10)
d=a%10
e=d/6
f=(no+e)*6
rate=b/c
print(f)
print(rate)


'''
'''run=int(input("enter"))
ball=float(input("wtydgi"))
ne=ball//1
rem=(ball*10)%10
balls=(ne*6)+rem
rate=(run/balls)*6
print(rate)
print(balls)'''
'''
'''


'''
---

Assignment 8: Compound Interest

A person invests money in a bank that provides compound interest annually.

Input:
Principal = 10000
Rate = 5%
Time = 2 years

Expected Output:
Amount after interest = 11025.0

p,r,t=map(float,input("Enter the  runs and over").split(","))
am=p*(1+r/100)**t
print(am)

---

Assignment 9: Petrol Cost Calculation

You traveled a certain distance. Based on mileage and petrol price, calculate fuel used and total cost.

Input:
Distance = 450 km
Mileage = 15 km/litre
Petrol price = 110/litre

Expected Output:
Petrol Used = 30.0 litres
Total Cost = 3300.0

dis=int(input("Enter the distance and (in km):"))
mil=int(input("Enter the Milage (in km/l):"))
petrol=int(input("Enter the Petrol price:"))
price=dis//mil*petrol
cost=price*petrol
print(price)
print(cost)

---

Assignment 10: Time Conversion

Convert total seconds into hours, minutes, and seconds.

Input:
Total seconds = 7384

Expected Output:
Hours = 2
Minutes = 3
Seconds = 4

sec=int(input("Enter sec:"))
hr=sec//3600
hr1=sec%3600
min=hr1//60
min1=hr1%60
sec=min1
print(hr)
print(min)
print(sec)

---

Assignment 11: Expression Evaluation

A billing system applies nested calculations with discounts and extra charges using brackets and unary operators.

Input:
50 + (10 * (+(2**3))) / 4 - (-6 % 4)
print(50 + (10 * (+(2**3))) / 4 - (-6 % 4))


---

Assignment 12: Expression Evaluation

A gaming score system calculates bonus points using exponent and applies penalties using unary negative values and brackets.

Input:

x=100 - (20 * (3**2)) + (40 / (+5)) - (-3)


print(x)

---

Assignment 13: Expression Evaluation

A shopping application applies offers using exponent and grouped calculations with unary adjustments.

Input:
x=25 + (5 * (6**2) // 3) - (-(8 % 5)) + (+2)
print(x)
---

Assignment 14: Expression Evaluation

A travel fare calculator computes total fare using grouped operations, power calculations, and unary adjustments.

Input:
x=(80 / (4 * 2)) * (+(2**2)) + 15 - (-(9 % 2))
prnit(x)
---

Assignment 15: Expression Evaluation

An electricity billing system uses nested brackets, exponent-based scaling, and unary corrections.

Input:
x=60 + (12 * (2**3) // (+(4))) - (-(10 % 3))
print(x)
---

Assignment 16: Expression Evaluation

A performance evaluation system calculates final score using grouped operations, exponent, division, and unary adjustments.

Input:

x=45 + (15 * (2**2)) - (20 / (+(5))) + (-(7 % 3))
print(x)
---
'''