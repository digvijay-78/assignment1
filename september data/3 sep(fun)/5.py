"""QNO 5:Employee Data Processing System
A company stores information about its employees in two forms:
A list of employee ages.
A string containing employee names separated by spaces.
The HR department wants a Python application that can perform different operations on this data through a menu-driven system. To make the application modular and easy to maintain, each operation must be implemented using a separate function that accepts data as a parameter and returns the result.
Problem Statement
Develop a menu-driven Python application called Employee Data Processing System.
The program should allow the HR department to perform the following operations:
Functions on Employee Ages (List)
1. find_second_highest_age(age_list)
Accept a list of employee ages.
Return the second highest age.
2. count_senior_employees(age_list)
Accept a list of employee ages.
Consider employees aged 50 years or above as senior employees.
Return the count of senior employees.
3. remove_duplicate_ages(age_list)
Accept a list of employee ages.
Return a new list after removing duplicate ages while maintaining the original order.
Functions on Employee Names (String)
4. count_names_starting_with_vowel(names)
Accept a string containing employee names separated by spaces.
Return the number of names that start with a vowel (A, E, I, O, U).
5. longest_name(names)
Accept a string containing employee names separated by spaces.
Return the employee name having the maximum number of characters.
Menu
========== EMPLOYEE DATA PROCESSING SYSTEM ==========
1. Find Second Highest Employee Age
2. Count Senior Employees
3. Remove Duplicate Ages
4. Count Names Starting with a Vowel
5. Find Longest Employee Name
6. Exit
====================================
Enter your choice:
Sample Input
Employee Ages:
34 55 29 60 55 42 60 51
Employee Names:
Ajay Rahul Esha Omkar Ishita Neha
Sample Output
Second Highest Age : 55
Senior Employees : 4
Unique Ages : [34, 55, 29, 60, 42, 51]
Names Starting with Vowel : 3
Longest Employee Name : Ishita
Instructions
Implement all operations using separate functions.
Each function must accept parameters and return the result.
Do not print results inside the functions.
The menu should continue to appear until the user selects Exit.
Display an appropriate message for an invalid choice.
Use meaningful function and variable names and follow proper indentation"""
def second(age):
#	s=max(age)
#	age.remove(s)
#	return max(age)
	res=sorted(set(age),reverse=True)
	return res[1]
#age=list(map(int,input("enter the age ").split()))
def s(age):
	c=0
	for i in age:
		if i >=50:
			c+=1
	return c
def remove (age):
	res=[]
	for i in age:
		if i not in res:
			res.append(i)
	return res
def na(name):
	c=0
	for i in name:
		if i[0].lower() in "aeiou":
			c+=1
	return c
def long(name):
	s=0
	c="" 
	for i in name:
		if len(i)>s:
			s=len(i)
			c=i
	return c
name=list(map(str,input("enter the names").split()))
age=list(map(int,input("enter the age :").split()))
while True :
	print("""========== EMPLOYEE DATA PROCESSING SYSTEM ==========
1. Find Second Highest Employee Age
2. Count Senior Employees
3. Remove Duplicate Ages
4. Count Names Starting with a Vowel
5. Find Longest Employee Name
6. Exit
====================================""")
	ch=int(input("enter the choice"))
	match ch:
		case 1:
			print("Find Second Highest Employee Age")
			print("Second Highest Age :",second(age))
		case 2:
			print("Count Senior Employees")
			print("Senior Employees :",s(age))
		case 3:
			print(" Remove Duplicate Ages")
			print("Unique Ages : ",remove(age))
		case 4:
			print("Names Starting with Vowel :",na(name))
		case 5:
			print("Longest Employee Name :",long(name))
		case 6:
			print("Exit......")
			print("thankyou for visiting")
			break
		case _:
			print("Invalid choice")
