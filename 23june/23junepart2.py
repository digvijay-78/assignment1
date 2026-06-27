'''1. Insurance Claim Approval System

An insurance company processes claims based on policy age, claim amount, and accident type. 
The approval depends on multiple levels of verification to reduce fraud.

If the policy age is at least 2 years, then check the claim amount. If the claim amount is up to 50000,
then check the accident type. If it is minor, approve the claim; otherwise, approve it with inspection.
If the claim amount is between 50001 and 200000, then check the accident type. If it is major, approve with investigation;
otherwise reject. If the claim amount exceeds 200000, reject. If the policy age is less than 2 years,
then check accident type. If minor, reject; otherwise mark as pending review.

Input:
Policy Age = 3
Claim Amount = 120000
Accident Type = major

Output:
Claim Status = Approved with Investigation
age=int(input("enter the age"))
am=int(input("enter the amount"))
type=input("enter the accident type")

if age>2 and am<50000 and type.lower()=="minor":
    print("approve the claim")
elif age>2 and am<50000 and type.lower()!="minor":
    print("approve it with inspection")
elif age>2 and am>50000 and am<200000 and type.lower()=="major":
     print("approve it with inspection")
elif age>2 and am>50000 and am<200000 and type.lower()!="major":
     print("reject")
elif age>2 and am>200000:
     print("reject")
elif age<2 and type.lower()=="minor":
    print("reject")
else:
     print("pending")


2. University Admission System

A university decides admission based on marks, entrance score, and category of the student.

If marks are 70 or above, then check entrance score. If entrance score is 80 or above, then check category. If general, admit; otherwise admit with scholarship. If entrance score is less than 80, then check if marks are 85 or above. If yes, admit under management quota; otherwise reject. If marks are below 70, then check if category is not general and marks are at least 60. If yes, check entrance score. If it is 70 or above, waitlist; otherwise reject. If none of these conditions match, reject.

Input:
Marks = 72
Entrance Score = 85
Category = general

Output:
Admission Status = Admitted

marks = int(input("enter your marks : "))
score = int(input("enter your entrance score  : "))
category = input("category (SC/ST/OBC/General) : ")


if marks >= 70 :
    if score >=80 :
        if category.lower() == "general" :
            print("Admit")
        else:
            print("admit with scholarship")
    elif score < 80 :
        if marks >= 85 :
            print("admit under mang quota")
        else:
            print("reject")
else:
    if catogery != "general" and marks >=60 :
        if score >= 70 :
            print("waitlist")
        else:
            print("reject")
        
    else: 
       print("reject")

3. Smart Loan Risk Categorization

A bank categorizes loan applicants into risk levels based on salary, credit score, and number of existing loans.

If salary is at least 30000, then check credit score. If credit score is 750 or above, then check number of loans. If zero, assign low risk. If loans are up to 2, assign medium risk; otherwise high risk. If credit score is below 750, then check if salary is at least 50000. If yes, check if credit score is at least 650. If yes, medium risk; otherwise high risk. If salary is less than 30000, mark as not eligible.

Input:
Salary = 40000
Credit Score = 760
Existing Loans = 1

Output:
Risk Level = Medium Risk
salary = int(input("enter your salary : "))
credit = int(input("enter your credit score  : "))
loans =  int(input("enter number of loans : "))


if salary >= 30000 :
    if credit >= 750 :
        if loans == 0 :
            risk = "Low risk"
        elif loans <=2 :
            risk = "Medium risk"
        else :
            risk = "High risk"
    
    else : 
        if salary >= 50000 :
            if credit >= 650 :
                risk = "medium risk"
            else :
                risk = "High risk"
else : 
    print("Not eligible")

print("Risk level = ",risk)
4. E-Learning Course Access System

An online learning platform grants access based on subscription type, course progress, and test score.

If subscription is premium, then check progress. If progress is at least 80, then check test score. If score is at least 70, unlock certificate; otherwise allow retry. If progress is less than 80, ask to complete course. If subscription is basic, then check progress. If progress is at least 50, allow limited access; otherwise lock content. If subscription is neither, deny access.

Input:
Subscription = premium
Progress = 85
Test Score = 65

Output:
Access Status = Retry Test
sub = input("enter your subscription type premium/basic : ")
progress = int(input("enter your progress  : "))
score =  int(input("enter your score : "))


if sub.lower() == "premium" :
    if progress >= 80 :
        if score >= 70:
            print("unlock certificate")
        else:
            print("retry")
    else:  
        print("Complete the course")
elif sub.lower() == "basic" :
    if progress >= 50 :
        print("Limited acces")
    else :
        print("content is locked")

else :
    print("access denied")

5. Smart Warehouse Dispatch System

A warehouse decides dispatch strategy based on stock availability, priority level, and delivery distance.

If stock is at least 100, then check priority. If high priority, then check distance. If distance is up to 200, dispatch immediately; otherwise use fast courier. If priority is not high, then check if stock is at least 300. If yes, bulk dispatch; otherwise normal dispatch. If stock is less than 100, then check if stock is at least 50. If yes, and priority is high, partially dispatch; otherwise hold. If stock is below 50, mark out of stock.

Input:
Stock = 120
Priority = high
Distance = 300

Output:
Dispatch Status = Dispatch via Fast Courier'''
stock =  int(input("enter number of stocks : "))
priority = input("enter priority (high/low)").lower()
distance = int(input("enter distance : "))

if stock >= 100 :
    if priority == "high" :
        if distance <=200 :
            dispatch = "immediately"
        else:
            dispatch = "fast courier"
    else:
        if stock >= 300 :
            dispatch = "bulk dispatch"
        else :
            dispatch = "normal dispatch"
else :
    if stock >= 50 and priority == "high" :
        dispatch = "partially dispatch"
    elif stock < 50 and priority == "high" :
        dispatch = "hold"
    else :
        dispatch = "out of stock"

print("dispatch status = ",dispatch)