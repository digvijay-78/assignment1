"""1.
STUDENT RESULT MANAGEMENT SYSTEM
Scenario:
A college examination department wants to automate the process of generating student results. 
The staff should be able to enter student details, calculate marks, determine grades, and display a complete 
report card using a menu-driven application.
Develop a Python program using multiple user-defined functions and a menu-driven approach to perform the 
following operations.
MENU
1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Complete Result
6. Find Highest Subject Mark
7. Find Lowest Subject Mark
8. Exit
Functional Requirements
1. Add Student Details
   * Student Name
   * Roll Number
   * Marks of 5 Subjects
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Complete Result
6. Find Highest Subject Mark
7. Find Lowest Subject Mark
8. Exit
Grade Criteria
Percentage        Grade
90 - 100          A+
80 - 89           A
70 - 79           B
60 - 69           C
50 - 59           D
Below 50          Fail
Constraints
* Marks should be between 0 and 100.
* Display an appropriate message for invalid marks.
* The program should continue until the user chooses Exit.
Sample Input / Output
*** STUDENT RESULT MANAGEMENT ***
1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Result
6. Find Highest Mark
7. Find Lowest Mark
8. Exit
Enter Choice : 1
Enter Student Name : Ajay
Enter Roll Number : 101
Enter Mark 1 : 78
Enter Mark 2 : 85
Enter Mark 3 : 92
Enter Mark 4 : 88
Enter Mark 5 : 77
Student details added successfully.
Enter Choice : 2
Total Marks = 420
Enter Choice : 3
Percentage = 84.0
Enter Choice : 4
Grade = A
Enter Choice : 6
Highest Mark = 92
Enter Choice : 7
Lowest Mark = 77
Enter Choice : 5
----------- RESULT CARD -----------

Name        : Ajay
Roll Number : 101
Marks
Subject 1 : 78
Subject 2 : 85
Subject 3 : 92
Subject 4 : 88
Subject 5 : 77
Total Marks : 420
Percentage  : 84.0
Grade       : A
Highest Mark: 92
Lowest Mark : 77
Enter Choice : 8
Thank You. Program Terminated.
Important Instructions
1. The solution must be developed using multiple user-defined functions.
2. Use appropriate parameters wherever data needs to be passed between functions.
3. Use return statements wherever a function needs to send a result back to the caller.
4. Avoid using unnecessary global variables.
5. Implement the application using a menu-driven approach.
6. Perform proper input validation.
7. Write meaningful function names and maintain proper code readability.
"""
m=[]
pe=0
n=""
ro=0
while True:
   print("""*** STUDENT RESULT MANAGEMENT ***
1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Result
6. Find Highest Mark
7. Find Lowest Mark
8. Exit""")
   choice=int(input("enter your choice"))
   match choice:
      case 1:
         print("Add Student Details")
         name=input("ENTER THE NAME")
         n=name
         roll=int(input("Enter Roll Number :"))
         ro=roll
         def add():
               for i in range(5):
                     mark = int(input(f"Enter Mark {i+1} : "))
                     if 0 <= mark <= 100:
                        m.append(mark)
                     else:
                         print("Invalid Mark")
               return m
         add()
         print("Student details added successfully.")
      case 2:
           print("Calculate Total Marks")
           if len(m)==0:
               print("empty")
           
           def total(m):
               t=0
               for marks in m:
                   t=t+marks
               return t               
           print("Total Marks =",total(m))
      case 3:
            print( "Calculate Percentage")
            def per(m):
               p=sum(m)/(len(m))
               return p
            pe=per(m)
            print("Percentage =",pe)
      case 4:
          def grade(pe):
              if pe >= 90:
                  return "A+"
              elif pe >= 80:
                  return "A"
              elif pe >= 70:
                  return "B"
              elif pe >= 60:
                  return "C"
              elif pe >= 50:
                  return "D"
              else:
                  return "Fail"

          print(grade(pe)) 
      case 5:
         def display (m):
           print("Display Result")
           print("*"*5,"RESULT CARD","*"*5)
           print("name :",n)
           print("roll no. :",ro)
           print("marks")
           for i in range(len(m)):
               print("subject",i+1,":",m[i])
           print("total marks :",total(m))
           p=per(m)
           print("total percentage :",p)
           print("grade:",grade(p))
           print(max(m))
           print(min(m))
         display(m)
      case 6:
           print("Find Highest Mark")
           def ma(m):
               return max(m)
           print(ma(m))
      case 7:
           print("Find Lowest Mark")
           def mj(m):
               return min(m)
           print(mj(m))
      case 8:
           print("Thank You. Program Terminated.")
           break
      case _:
           print("invalid choice ")
