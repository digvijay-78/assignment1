'''1. Electricity Department Billing System


The electricity department of a city wants to automate the monthly bill generation process for its customers. The bill is calculated based on slab-wise unit consumption:

* First 100 units are charged at ₹5 per unit
* Next 100 units (101–200) are charged at ₹7 per unit
* Units above 200 are charged at ₹10 per unit

Write a Python program to calculate the total electricity bill based on the number of units consumed.

Input:
Enter units consumed: 250

Output:
Total Electricity Bill: ₹1950

a=int(input("enter the units:"))
if a<=100 :
		b=a*5
		print(b)
elif a>100 and a<200 :
		c= (a-100)*7+100*5
		print(c)
else:
	d=(a-200)*10+100*5+100*7
	print(d)


2. College Result Processing System


A college wants to generate grades for students automatically based on their marks in an exam. The grading criteria are as follows:

* 90 and above → Grade A
* 75 to 89 → Grade B
* 60 to 74 → Grade C
* 50 to 59 → Grade D
* Below 50 → Fail

Write a Python program to display the grade of a student.

Input:
Enter marks: 67

Output:
Grade: C

a=int(input("Enter marks: "))
if a>=90:
	print("grade A")
elif a<=89 and a>=75:
	print("grade b")
elif a>=60 and a<=74:
	print("grade c")
elif a>=50 and a<=59:
	print("grade d")
else:
	print("fail")




3. Income Tax Department System

The Income Tax Department needs a system to calculate tax payable by citizens based on their annual income:

* Up to ₹2,50,000 → No tax
* ₹2,50,001 to ₹5,00,000 → 5% tax
* ₹5,00,001 to ₹10,00,000 → 20% tax
* Above ₹10,00,000 → 30% tax

Write a Python program to calculate the tax amount.

Input:
Enter annual income: 800000

Output:
Tax Payable: ₹110000'''
'''
a=int(input("Enter tax: "))

if a<=250000:
	tax=0
elif a<=500000:
	tax=(a-250000)*5/100
elif a<=1000000:
	tax=((a-250000)*5/100)+(a-500000)*20/100
else:
	tax=((a-250000)*5/100)+((a-500000)*20/100)+(a-1000000)*30/100
print(tax)

a=int(input("Enter tax: "))
if a<=250000:
		print("no tax")
elif a>=250001 :
		per=a-250000
		per1=(per*5/100)
		print("tax payable",per1)
elif a>=500001 :
		per2=a-250000 
		per3=(per2*5/100)
		per4=a-500000
		per5=(per4*20/100)
		print("tax payable",per5)
else:
		per6=a-250000 
		per7=(per6*5/100)
		per8=a-500000
		per9=(per8*20/100)
		per10=a-1000000
		per11=(per10*30/100)
		print("tax payable",per11)
	
'''

		


'''

4. E-Commerce Discount Engine


An online shopping platform provides discounts to customers based on their total purchase amount:

* Above ₹5000 → 20% discount
* ₹2000 to ₹5000 → 10% discount
* Below ₹2000 → 5% discount

Write a Python program to calculate the final amount after discount.

Input:
Enter purchase amount: 4500

Output:
Final Amount: ₹4050

a=int(input("Enter  amount: "))

if a>=5000:
	dis =a - (a*20/100)
elif a>=2000:
	dis=a - (a*10/100)
else:
	dis=a - (a*5/100)
print("final amount is" ,dis)

5. Cinema Ticket Booking System


A cinema hall charges ticket prices based on the age of the customer:

* Children (below 12 years) → ₹100
* Adults (12 to 60 years) → ₹200
* Senior citizens (above 60 years) → ₹150

Write a Python program to determine the ticket price.

Input:
Enter age: 10

Output:
Ticket Price: ₹100

age=int(input("Enter  age: "))
if age<=12:
	print("Ticket Price: ₹100")
elif age<=60:
	print("Ticket Price: ₹200")
else:
	print("Ticket Price: ₹150")


6. Company Bonus Distribution System


A company wants to calculate bonuses for employees based on their years of experience:

* More than 10 years → 20% bonus
* 5 to 10 years → 10% bonus
* 2 to 5 years → 5% bonus
* Less than 2 years → No bonus

Write a Python program to calculate the bonus amount.

Input:
Enter salary: 50000
Enter years of experience: 6

Output:
Bonus Amount: ₹5000

sal=int(input("Enter  salary: "))
year=int(input("Enter  years of experience: "))
if year>=10:
	s=sal*20/100
	print("bonus amount=",s)
elif year>=5:
	s=sal*10/100
	print("bonus amount=",s)
elif year>=2:
	s=sal*5/100
	print("bonus amount=",s)
else:
	print("no bonus")


7. Banking Withdrawal Limit System


A bank wants to set withdrawal limits based on the available account balance:

* Balance less than ₹1000 → Withdrawal not allowed
* ₹1000 to ₹5000 → Maximum withdrawal ₹1000
* Above ₹5000 → Maximum withdrawal ₹5000

Write a Python program to display the withdrawal limit.

Input:
Enter account balance: 3500

Output:
Maximum Withdrawal Limit: ₹1000

bal=int(input("Enter  account balance: "))
if age<=1000:
	print("Withdrawal not allowed")
elif age<=5000:
	print(" Maximum withdrawal ₹1000")
else:
	print("Maximum withdrawal ₹5000")


8. Weather Monitoring System

A weather monitoring system classifies the weather condition based on temperature:

* Below 0°C → Freezing
* 0°C to 20°C → Cold
* 21°C to 35°C → Warm
* Above 35°C → Hot

Write a Python program to classify the weather.

Input:
Enter temperature: 38

Output:
Weather Condition: Hot


tem=int(input("Enter temp: "))
if tem>35:
	print("Weather Condition: Hot")
elif tem>=21:
	print(" Weather Condition: warm")
elif tem>=0:
	print(" Weather Condition: cold")
else:
	print("Weather Condition:frezzing")



9. Student Attendance Eligibility System

A college determines whether a student is eligible to sit for exams based on attendance percentage:

* 75% and above → Eligible
* 60% to 74% → Eligible with warning
* Below 60% → Not eligible

Write a Python program to check eligibility.

Input:
Enter attendance percentage: 58

Output:
Status: Not Eligible

att=int(input("Enter attendance percentage: "))
if att>75:
	print(" Eligible")
elif att>=60:
	print("Eligible with warning")
else:
	print("Not eligible")


10. Mobile Data Plan Advisor


A telecom company suggests the most suitable data plan based on a user’s daily data usage:

* More than 3GB/day → Premium Plan
* 1GB to 3GB/day → Standard Plan
* Less than 1GB/day → Basic Plan

Write a Python program to recommend a plan.

Input:
Enter daily data usage: 0.8

Output:
Recommended Plan: Basic Plan


gb=float(input("Enter daily data usage: "))
if gb>3:
	print(" Premium Plan")
elif gb>=1:
	print(" Standard Plan")
else:
	print("basic plan")




11. Railway Ticket Fare System


A railway system calculates ticket fare based on distance and travel class:

* Distance ≤100 km:
  Sleeper → ₹100, AC → ₹200
* Distance 101–500 km:
  Sleeper → ₹300, AC → ₹600
* Distance >500 km:
  Sleeper → ₹500, AC → ₹1000

Write a Python program to calculate ticket fare.

Input:
Enter distance: 350
Enter class: AC

Output:
Total Fare: ₹600

dis=int(input("Enter  distance : "))
classs=input("enter  class:")
if dis<=100 and classs.lower()=="ac":
	print("total fare:200")
elif dis<=100 and classs.lower()=="sleeper":
	print("total fare:100")

elif dis<=500 and classs.lower()=="ac":
	print("total fare:600")
elif dis<=500 and classs.lower()=="sleeper":
	print("total fare:300")
else:
	if dis>=500 and classs.lower()=="ac":
		print("total fare:1000")
	else:
		dis>=500 and classs.lower()=="sleeper"
		print("total fare:500")



12. Restaurant Bill with GST System

A restaurant applies GST based on the total bill amount:

* Up to ₹1000 → 5% GST
* ₹1001 to ₹5000 → 12% GST
* Above ₹5000 → 18% GST
  Additionally, if the bill exceeds ₹3000, a service charge of ₹200 is added.

Write a Python program to calculate the final bill.

Input:
Enter bill amount: 4000

Output:
Final Bill Amount: ₹4680'''
bill=int(input("enter the bill")
if bill<=1000:
	a=bill + (bill*5/100)
elif bill<=5000 and bill>=3000:
	a=(bill-1000-*5/100)+(bill-1000)*12/100)+200
elif bill<=5000 and 

'''

13. Employee Performance Appraisal System


A company evaluates employees based on performance rating (1–5):

* 5 → 25% salary hike
* 4 → 20% salary hike
* 3 → 10% salary hike
* 2 → 5% salary hike
* 1 → No hike
  If salary is below ₹20000 and rating is 4 or above, an additional ₹2000 bonus is given.

Write a Python program to calculate revised salary.

Input:
Enter salary: 18000
Enter rating: 4

Output:
Revised Salary: ₹23600

14. Online Course Fee System

An online platform offers courses with fixed fees:

* Programming → ₹5000
* Design → ₹4000
* Marketing → ₹3000
  Discount is applied based on user type:
* Student → 20% discount
* Working Professional → 10% discount
* Others → No discount

Write a Python program to calculate final course fee.

Input:
Enter course category: Programming
Enter user type: Student

Output:
Final Course Fee: ₹4000

15. Smart Parking System

A smart parking system charges based on vehicle type and parking duration:

* Bike → ₹10/hour
* Car → ₹20/hour
* Bus → ₹50/hour
  If parking duration exceeds 5 hours, an additional ₹100 penalty is applied.

Write a Python program to calculate total parking fee.

Input:
Enter vehicle type: Car
Enter hours parked: 6

Output:
Total Parking Fee: ₹220'''