'''1. Smart Voting & ID Verification System
   A government system verifies whether a citizen can vote and whether they have a valid ID.

* If age ≥ 18 → Eligible to vote
* If ID proof is available → Allowed inside booth

Input:
Enter age: 22
Do you have ID (yes/no): yes

Output:
Eligible to vote
Allowed inside booth

age=int(input("enter the age:"))
id=input("enter the ID(yes/no):")
if age>=18:
	if id.lower()=="yes":
		print("eligibe to vote\nAllowed inside booth" )
	else:
		print("must be decline")
else:
	print("underage")


2. Student Performance Analyzer
   A school wants to evaluate students based on marks.

* If marks ≥ 40 → Pass
* If marks ≥ 75 → Distinction

Input:
Enter marks: 80

Output:
Pass
Distinction

marks=int(input("enter the marks:"))
if marks >= 40:
	if marks >= 75:
		print("Pass\nDistinction")
	else:
		print("pass")
else:
	print("fail")
		

'''
'''
3. E-Commerce Offer Engine
   An online store provides multiple offers independently:

* If cart value ≥ 500 → Free delivery
* If cart value ≥ 1000 → 10% discount coupon

Input:
Enter cart value: 1200

Output:
Free delivery applied
Discount coupon unlocked

value=int(input("enter the cart value:"))
if value >=500:
	if value >=1000 :
		print("Free delivery applied\nDiscount coupon unlocked")
	else:
		print("Free delivery applied")
else:
	print("thankyou")


4. Gym Membership Eligibility Checker
   A gym checks multiple conditions:

* If age ≥ 18 → Allowed for gym
* If BMI > 25 → Suggest weight loss program

Input:
Enter age: 25
Enter BMI: 27

Output:
Gym access granted
Enroll in weight loss program

age=int(input("enter the age:"))
bmi=int(input("enter the BMI:"))
if age>=18:
	if bmi>=25:
		print("Gym access granted\nEnroll in weight loss program")
	else:
		print("Gym access granted,but not satisfied the BMI")
else:
	print("not granted")
	

5. Banking Security System
   A bank validates login attempt:

* If username is "admin" → Valid user
* If password length ≥ 8 → Strong password

Input:
Enter username: admin
Enter password: secure123

Output:
Valid user
Strong password

username=input("enter the username:")
password =input("enter the password:")
if username=="admin":
	if password=="secure123":
		print("Valid user\nStrong password")
	else:
		print("wrong password")
else:
	print("wrong username")



6. Weather Monitoring System
   A system checks weather conditions:

* If temperature ≥ 30 → Hot day
* If humidity ≥ 70 → High humidity alert

Input:
Enter temperature: 32
Enter humidity: 75

Output:
Hot day
High humidity alert

temp=int(input("enter the temp:"))
hum=int(input("enter the humidity:"))
if temp>=30:
	print("Hot day")
else:
	print("normal day")
if hum>=75:
	print("High humidity alert")
else:
	print("normal")





7. Salary Benefits System
   A company provides benefits:

* If salary ≥ 30000 → Eligible for PF
* If salary ≥ 50000 → Eligible for bonus

Input:
Enter salary: 55000

Output:
PF applicable
Bonus applicable


sal=int(input("enter the salary:"))
if sal>=30000:
	if sal>=50000:
		print("PF applicable\nBonus applicableh" )
	else:
		print("PF applicable")
else:
	print("no previlage")



8. Number Property Checker
   A system evaluates number properties:

* If number % 2 == 0 → Even number
* If number % 5 == 0 → Divisible by 5

Input:
Enter number: 20

Output:
Even number
Divisible by 5

num=int(input("enter the no.:"))

if num%2==0:
	if num%5==0:
		print("Even number\nDivisible by 5" )
	else:
		print("only even")
else:
	print("odd no.")

9. Library Access System
   A library checks:

* If membership is active → Entry allowed
* If books issued < 3 → Can issue more books

Input:
Membership active (yes/no): yes
Books issued: 2

Output:
Entry allowed
Can issue more books




mem=input("enter the membership(yes/no):")
book=int(input("enter the books issued:"))
if id.lower()=="yes":
	if book<3:
		print("Entry allowed\nCan issue more books" )
	else:
		print("membership active but can't issue more books")
else:
	print("expired membership")



10. Online Exam System
    System evaluates exam conditions:

* If marks ≥ 40 → Pass
* If attendance ≥ 75 → Eligible for certificate

Input:
Enter marks: 60
Enter attendance: 80

Output:
Pass
Eligible for certificate



marks=int(input("enter the marks:"))
if marks>=40:
	if marks>=75:
		print("Pass\nEligible for certificate" )
	else:
		print("pass")
else:
	print("fail")





NESTED IF ELSE:--
NOTE: Complete all the following assignments using Nested if-else statements only.

1. A bank wants to automate its loan approval process. The system should take salary,
credit score, and number of existing loans as input. If the salary is greater than or equal to 30000,
then it should check the credit score. If the credit score is greater than or equal to 750,
 the loan should be approved. Otherwise, it should check the number of existing loans.
If the existing loans are less than 2, the loan should be conditionally approved; otherwise, it should be rejected.
If the salary is less than 30000, the loan should be rejected. Display the final loan status.

Input:
Salary = 40000
Credit Score = 720
Existing Loans = 1

Output:
Loan Status = Conditional Approval

salary,cr,loan=map(int,input("enter the marks:").split(","))
if salary>=30000:
	if cr>=750:
		print("Loan Status = Conditional Approvale" )
	else:
		if not(cr>=750) and loan<=2:
			print("conditionally approved")
		else:
			print("loan condition not meet")
			
		
else:
	print("loan rejected")

2. An e-commerce website provides discounts based on the cart value and user type.
The system should take cart value and user type (premium or regular) as input.
 If the cart value is greater than or equal to 5000, then check the user type. If the user is premium,
 apply a 20% discount; otherwise, apply a 10% discount. If the cart value is less than 5000,
then check if it is greater than or equal to 2000. If yes, apply a 5% discount; otherwise,
no discount is applied. Display the final payable amount.

Input:
Cart Value = 6000
User Type = Premium

Output:
Final Amount = 4800

value=int(input("cart value"))
name=input("enter the user type (premium or regular):")
if value>=5000:
    if name.lower()=="premium":
        value1=value*20/100
        value2=value-value1
        print("final amount=",value2)
    else:
        value3=value*10/100
        value4=value-value3
        print("final amount=",value4)
else:
    if value>=2000:
          value5=value*5/100
          value6=value-value5
          print("final amount=",value6)
    else:
        print("no discount is applied",value)


3. A smart electricity monitoring system categorizes usage levels for better energy management.
The system should take the number of units consumed as input. If the units are greater than or equal to 100, then check further.
 If the units are greater than or equal to 300, assign "High Usage". Otherwise, check again.
If the units are greater than or equal to 200, assign "Moderate Usage"; otherwise, assign "Normal Usage".
 If the units are less than 100, assign "Low Usage". Display the usage category.

Input:
Units = 220

Output:
Usage Category = Moderate Usage

unit=int(input("unit"))
if unit>=100:
    if unit>=300:
        print("high usage")
    else:
        if unit>=200:
                  print("moderate")
        else:
               print("normal usage")
else:
    print("low usage")
        
                  


4. A gym provides personalized plans based on age, weight, and fitness goal.
The system should take age, weight, and goal (weight loss or muscle gain) as input.
 If the age is greater than or equal to 18, then check the weight. If the weight is greater than or
 equal to 80, then check the goal. If the goal is "weight loss", assign "Cardio Plan"; otherwise, assign
"Strength Plan". If the weight is less than 80, assign "General Fitness Plan". If the age is less than 18, display
 "Not Allowed". Display the recommended plan.

Input:
Age = 25
Weight = 85
Goal = weight loss

Output:
Plan = Cardio Plan

age=int(input("age?"))
weight=int(input("weight"))
goal=input("enter the goal (weight loss or muscle gain):")
if age>=18:
    if weight>=80:
    	if goal.lower()=="weight loss":
            print("cardio plan")
        else:
            print("strenght plan")
    else:
    	if weight<80:
        	print("General Fitness Plan")
else:
	 print("not allowed")





5. An ATM system processes withdrawal requests. The system should take account balance,
 withdrawal amount, and PIN status (correct or incorrect) as input. If the balance is
greater than or equal to the withdrawal amount, then check the withdrawal limit.
If the withdrawal amount is less than or equal to 10000, then check the PIN.
 If the PIN is correct, display "Transaction Successful"; otherwise, display "Invalid PIN".
If the withdrawal amount exceeds 10000, display "Limit Exceeded". If the balance is less than the
 withdrawal amount, display "Insufficient Balance".

Input:
Balance = 20000
Withdrawal Amount = 8000
PIN = correct

Output:
Transaction Successful


bal=int(input("balnce?"))
ammo=int(input("withdrawl ammount"))
pin=input("enter the pin:")
if bal>=ammo:
	if ammo<=10000:
		if pin.lower()=="1234567a":
			print("Transaction Successful")
		else:
			print("invalid")
    else:
    	print("limit exceeded")
else:
	 print("insufficient balnace")




6. A movie theatre calculates ticket prices based on age, show time, and day type.
 The system should take age, show time (morning/evening), and day type (weekday/weekend) as input.
If the age is less than 18, then check the show time. If the show time is morning, ticket price is 100; otherwise, ticket price is 150.
 If the age is 18 or above, then check the show time. If the show time is evening,
then check the day type. If it is weekend, ticket price is 300; otherwise, 250.
 If the show time is not evening, ticket price is 200. Display the ticket price.

Input:
Age = 25
Show Time = evening
Day = weekend

Output:
Ticket Price = 300




age = int(input("Age : "))
time = input("show time (morning/evening) : ")
day = input("which day (weekday/weekend) : ")

if age >= 18 :
    if time == "evening" :
        if day == "weekend" :
            print("Ticket price is 300")
        else : 
            print("Ticket price is 250")
    else : 
        print("Ticket price is 250")
            
else :
    if time == "morning" :
        print("Ticket price is 100")
    else:
        print("Ticket price is 150")

7. A company calculates employee bonuses based on experience,
 performance rating, and salary. The system should take experience (in years), rating, and salary as input.
If the experience is greater than or equal to 5, then check the rating. If the rating is greater than or equal to 4, then check the salary.
 If the salary is less than 50000, assign a 20% bonus; otherwise, assign a 10% bonus. If the rating is less than 4, assign a 5% bonus.
 If the experience is less than 5, no bonus is given. Display the bonus amount.

Input:
Experience = 6
Rating = 4
Salary = 40000

Output:
Bonus = 8000


experience = int(input("enter your experience in years : "))
rating = int(input("enter your rating : "))
salary = int(input("enter your salary : "))

bonous = 0

if experience >= 5 :
    if rating >= 4 :
        if salary < 50000 :
            bonous = (salary*20)/100
        else : 
            bonous = (salary*10)/100
    else :
        bonous = (salary*5)/100
else :
    print("NO bonous")

print("Bonous =",bonous)


8. A warehouse management system needs to identify the highest stock level among six different storage units to prioritize dispatch.
 The system should take the quantity of items stored in six units as input. It should compare all six values using nested conditions
 and determine which unit has the maximum stock. Display the highest stock value among all six units.

Input:
Unit1 = 120
Unit2 = 450
Unit3 = 300
Unit4 = 275
Unit5 = 500
Unit6 = 390

Output:
Highest Stock = 500'''

a = int(input("enter unit1 = ")) 
b = int(input("enter unit2 = "))
c = int(input("enter unit3 = "))
d = int(input("enter unit4 = "))
e = int(input("enter unit5 = "))
f = int(input("enter unit6 = "))
'''a = 100
b= 1200 
c=1000
d =140
e = 150
f = 170
'''

if a>b :
    if a>c :
        if a>d :
            if a>e :
                if a>f:
                    print("unit1 is greater")
                else:
                    print("unit6 is greater")
            else : 
                if e>f :
                    print("unit5 is greater")
                else :
                    print("unit6 is greater")
        else: 
            if d>e :
                if d>f :
                    print("unit4 is greater")
                else:
                    print("unit6 is greater")
            else : 
                if e>f :
                    print("unit5 is greater")
                else :
                    print("unit6 is greater")
                
    else:
        if c>d :
            if c>e :
                if c>f :
                   print("unit3 is greater")
                else:
                   print("unit6 is greater")
            else:
                if e>f :
                    print("unit5 is graeter")
                else:
                    print("unit6 is greater")
        else:    
            if d>e :
                if d>f :
                    print("unit4 is greater")
                else : 
                    print("unit6 is greater")
            else :
                if e>f :
                    print("unit5 is greater")
                else :
                    print("unit6 is greater")



else :
    if b>c :
        if b>d :
            if b>e :
                if b>f:
                    print("unit2 is greater")
                else:
                    print("unit6 is greater")
            else : 
                if e>f :
                    print("unit5 is greater")
                else :
                    print("unit6 is greater")
        else: 
            if d>e :
                if d>f :
                    print("unit4 is greater")
                else:
                    print("unit6 is greater")
            else : 
                if e>f :
                    print("unit5 is greater")
                else :
                    print("unit6 is greater")
                
    else:
        if c>d :
            if c>e :
                if c>f :
                   print("unit3 is greater")
                else:
                   print("unit6 is greater")
            else:
                if e>f :
                    print("unit5 is graeter")
                else:
                    print("unit6 is greater")
        else:    
            if d>e :
                if d>f :
                    print("unit4 is greater")
                else : 
                    print("unit6 is greater")
            else :
                if e>f :
                    print("unit5 is greater")
                else :
                    print("unit6 is greater")