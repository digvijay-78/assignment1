'''1. Utility Toolkit System

You are developing a Utility Toolkit Application for a small office. Employees use this tool to quickly perform common number operations like checking prime numbers, reversing numbers, etc.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Check Prime Number
2 → Check Palindrome Number
3 → Reverse a Number
4 → Count Digits
5 → Exit

Sample Run 1:
Input:
Enter your choice: 1
Enter number: 7

Output:
7 is a Prime Number

Sample Run 2:
Input:
Enter your choice: 2
Enter number: 121

Output:
121 is a Palindrome Number

Sample Run 3:
Input:
Enter your choice: 3
Enter number: 456

Output:
Reversed Number is: 654

Sample Run 4:
Input:
Enter your choice: 4
Enter number: 98765

Output:
Total digits: 5

Sample Run 5 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

Sample Run 6 (Exit):
Input:
Enter your choice: 5

Output:
Exiting program... Thank you!

Requirements:

* Use while loop to repeat menu
* Use match-case for decision making
* Handle negative numbers properly
* Use only loops and conditions
'''
while True:
	print("Menu Options:\n1 → Check Prime Number\n2 → Check Palindrome Number\n3 → Reverse a Number\n4 → Count Digits\n5 → Exit")
	choice=int(input("Enter the choice:"))
	match choice:
		case 1:
			a=int(input("enter no."))
			if a<=1:
				print("not")
			else:
				for i in range(2,a//2):
					if a%i==0:
						print("not a prime")
						break
				else:
					print("prime")
		case 2:
			a=int(input("enter no."))
			n=a
			rev=0
			for i in range(len(str(a))):
				d=a%10
				rev=rev*10+d
				a=a//10
			if n==a:
				print("Palindrome Number")
			else:
				print("Not a Palindrome Number")
		case 3:
			a=int(input("enter no."))
			n=a
			rev=0
			for i in range(len(str(a))):
				d=a%10
				rev=rev*10+d
				a=a//10
			print(rev)
		case 4:
			a=int(input("enter no."))
			count=0
			for i in range(len(str(a))):
				d=a%10
				count=count+1
				a=a//10
		case 5:
			print("Exiting program... Thank you!")
			break
		case __:
			print("invalid choice. Please try again.")
			break