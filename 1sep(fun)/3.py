# """3.
# ONLINE SHOPPING SYSTEM
# Scenario:
# An e-commerce company wants to develop an Online Shopping System.
#  The application should be menu-driven and should demonstrate different types of arguments used in Python functions.
# MENU
# 1. Customer Registration
# 2. Product Information
# 3. Generate Invoice
# 4. Add Multiple Products
# 5. Display Customer Profile
# 6. Exit
# Requirements
# Choice 1 – Customer Registration
# * Accept Customer Name, Email, and Mobile Number.
# * Pass the values to a function using Positional Arguments.
# * Display the registered customer details.
# Choice 2 – Product Information
# * Accept Product Name, Price, and Category.
# * Call the function using Keyword Arguments.
# * Display the product details.
# Choice 3 – Generate Invoice
# * Accept Product Name and Price.
# * Tax Percentage should have a default value.
# * Use Default Arguments while generating the invoice.
# * Display the final amount.
# Choice 4 – Add Multiple Products
# * Allow the user to enter any number of product prices.
# * Pass all prices to a function using Variable Length Arguments (*args).
# * Calculate and display the total bill amount.
# Choice 5 – Display Customer Profile
# * Accept any number of customer details such as Name, City, Email, Mobile, Membership Type, etc.
# * Pass the details using Arbitrary Keyword Arguments (**kwargs).
# * Display all customer information.
# Choice 6 – Exit
# Sample Execution
# Enter Choice : 1
# Enter Name : Ajay
# Enter Email : [ajay@gmail.com](mailto:ajay@gmail.com)
# Enter Mobile : 9876543210
# Customer Registered Successfully
# Enter Choice : 2
# Enter Product Name : Laptop
# Enter Price : 55000
# Enter Category : Electronics
# Product Details Displayed Successfully
# Enter Choice : 3
# Enter Product Name : Laptop
# Enter Price : 55000
# Invoice Generated Successfully
# Enter Choice : 4
# Enter Number of Products : 4
# Enter Price 1 : 100
# Enter Price 2 : 200
# Enter Price 3 : 300
# Enter Price 4 : 400
# Total Bill Amount : 1000
# Enter Choice : 5
# Customer Profile Displayed Successfully
# Enter Choice : 6
# Thank You. Program Terminated.
# Important Instructions
# 1. Choice 1 must use Positional Arguments.
# 2. Choice 2 must use Keyword Arguments.
# 3. Choice 3 must use Default Arguments.
# 4. Choice 4 must use Variable Length Arguments (*args).
# 5. Choice 5 must use Arbitrary Keyword Arguments (**kwargs).
# 6. Use separate functions for each menu option.
# 7. Implement the solution using a menu-driven approach.
# 8. Maintain proper code readability and formatting.
# Note:
# Marks will be awarded based on the correct usage of the specified argument type in each menu option."""

# def customer(name,email,no):
# 	print("name is ",name,"email of the ",name,"is ",email,no)
# def product (pname,price,cat):
# 	print(pname,price,cat)
# def gen (name="ash",price=10,tax=30):
# 	print(name,price)	
# 	print(price*tax/100+price)
# def multi (*pro):
# 	t=0
# 	for i in range (len(pro)):
# 		t+=pro[i]
# 	return t
# def display (**a):
# 	for key,value in a.items ():
# 		print(key ,":",value)

# while True:
# 	print("""******** ONLINE SHOPPING SYSTEM ********
#  1. Customer Registration 
# 2. Product Information 
# 3. Generate Invoice 
# 4. Add Multiple Products 
# 5. Display Customer Profile 
# 6. Exit """)
# 	choice =int (input ("enter the choice"))
# 	match choice :
# 		case 1:
# 			name=input ("enter the name")
# 			email=input("enter the email")
# 			no=int(input("enter the number"))
# 			customer (name,email,no)
# 		case 2:
# 			pname = input("Enter Product Name : ")
# 			price = float(input("Enter Price : "))
# 			cat=input("enter the category")
# 			product(pname=pname,price=price,cat=cat)
# 		case 3:
# 			name = input("Enter Product Name : ") 
# 			price = float(input("Enter Price : "))
# 			gen(name,price)
# 		case 4 :
# 			n = int(input("Enter Number of Products : "))
# 			pro=[]
# 			for i in range (n):
# 				price =float(input("enter Price "+str(i+1)+":"))
# 				pro.append(price)
# 			total=multi(*pro)
# 			print("total bill amount :",total )
# 		case 5 :
# 			name = input("Enter Name : ") 
# 			city = input("Enter City : ") 
# 			email = input("Enter Email : ") 
# 			no = input("Enter Mobile Number : ") 
# 			member = input("Enter Membership Type : ")
# 			display(name=name,city=city,email=email,member=member)
# 		case 6 :
# 			print("Thank You. Program Terminated.")
# 			break
# 		case _:
# 			print("invalid")

