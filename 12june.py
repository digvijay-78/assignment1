#1. Hello & Name Printer
#Write a program to print:
#Hello
#Your Name

print("Hello")
print("Digvijay Chouhan")



'''2. Menu Display
Write a program to display:
=== Welcome to Coffee Shop ===
1. Espresso     $3
2. Latte        $4
3. Cappuccino   $5'''


print("===Welcome to Coffee Shop===")
print ("1.Espresso     $3\n2. Latte        $4\n3. Cappuccino   $5")


'''3. Resume Format
Write a program to display:
=== Resume ===
Name       : Alice Johnson
Email      : alice@example.com
Skills     :
  - Java
  - HTML & CSS
  - Problem Solving
Experience : 2 years at XYZ Ltd.'''

print("=== Resume ===")
name= "Alice Johnson"
email="alice@example.com"
experience="2years at XYZ ltd."


print(f"Name :{name}\nEmail :{email}")
print("Skills :\n-java\n-HTML&CSS\n-Poblem Solving")
print(f"Experience :{experience }")


'''4. Star Pattern(without loop)
Write a program to print:
***
***
***'''
print(f"***\n***\n***")

'''5. Special Characters
Write a program to print:
@ # $ % ^ & *
'''
print("@ # $ % ^ & *")

'''6. Print User Details
Take input:
- Name
- Age
- City
Display them properly.
'''
'''name=input("Enter The Name: ")
age=int(input("Enter The Age:"))
city=input("Enter The City:")
print(f"Details of the user are:\nName:{name}\nAge:{age}\nCity:{city}")
'''
'''
7. Full Name Display
Take first name and last name as input and display:
Full Name: John Doe'''
'''
a=input("Enter The first name :")
b=input("Enter The second name :")
c=(a+" "+b)
print("Full Name:", c)'''
'''8. Simple Input Display
Take two numbers as input and print them on separate lines.'''

print(10,20,sep="\n")

'''9. Three Inputs Display
Take three values from user and print each on new line.'''
'''
n1= int(input("values"))
n2= int(input("values"))
n3= int(input("values"))
print(n1)
print(n2)
print(n3)'''

'''10. Input and Echo
Take input from user and print:
You entered: <input>'''
#j=input("Enter ")
#print("You entered:<{}>".format(j))

'''
11. Greeting Message
Take name as input and print:
Hello <name>
Welcome to Python'''
'''
name=input("Enter The Name:")
print("Hello:<{}>\nWelcome to Python".format(name))
'''
'''
12. Favorite Things
Take input:
- Favorite food
- Favorite color
Display:
I like <food> and my favorite color is <color>'''
'''
food=input("Enter The Favorite food:")
color=input("Enter The Favorite color:")
print("I like <{}> and my favorite color is <{}>".format(food,color))
'''
'''
13. College Details
Take input:
- College Name
- Course
- Year
Display in proper format.'''
clg_name=input("Enter the name of College:")
clg_course =input("Enter the name of Course:")
clg_year=int(input("Enter the year:"))

print("The college name is :{}\ncourse is:{}\nin year:{}".format(clg_name,clg_course,clg_year))
'''
14. Email Display
Take email as input and print:
Your email is: <email>'''
email=input("Enter your email:")
print(f"your e mail is:{email}")
'''
15. Bio Data
Take input:
- Name
- Age
- Phone
Display:
--- Bio Data ---
Name  :
Age   :
Phone :'''

name=input("Enter the name :")
age=int(input("Enter the age:"))
phone_no=int(input("Enter the phone no.:"))
print("--- Bio Data ---")
print(f"Name  :{name}\nAge   :{age}\nPhone :{phone_no}")



