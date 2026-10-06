'''2.

=========================================================
            MATRIX ANALYSIS SYSTEM
=========================================================


A research laboratory stores experimental data in matrix form.
Scientists want a program that can analyze the matrix and provide
different statistics through a menu-driven application.

The application should allow the user to:

1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Count Prime Numbers Row-wise
   2. Count Perfect Numbers Column-wise
   3. Display Row-wise Sum
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Count Prime Numbers Row-wise
   ---------------------------------------
   Count and display the number of prime numbers present
   in each row of the matrix.

5. Choice 2 - Count Perfect Numbers Column-wise
   --------------------------------------------
   Count and display the number of perfect numbers present
   in each column of the matrix.

   Note:
   A perfect number is a number that is equal to the sum
   of its proper divisors.

   Examples:
   6  = 1 + 2 + 3
   28 = 1 + 2 + 4 + 7 + 14

6. Choice 3 - Display Row-wise Sum
   --------------------------------
   Calculate and display the sum of each row.

7. Choice 4 - Exit
   --------------------------------
   Display:
   "Thank You for Using Matrix Analysis System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 1

Enter rows: 3
Enter columns: 3

Enter matrix elements:
2 4 5
6 7 8
11 28 13

Output:
Row 1 Prime Count = 2
Row 2 Prime Count = 1
Row 3 Prime Count = 2

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 2

Output:
Column 1 Perfect Number Count = 1
Column 2 Perfect Number Count = 1
Column 3 Perfect Number Count = 0

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 3

Output:
Row 1 Sum = 11
Row 2 Sum = 21
Row 3 Sum = 52

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 4

Output:
Thank You for Using Matrix Analysis System

=========================================================

'''
import math
print("MATRIX ANALYSIS SYSTEM")
while True:
   print("-"*32)
   print("MENU")
   print('''1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit''')
   a=int(input("ENTER YOUR CHOICE"))

   match a:
      case 1:
         print("Count Prime Numbers Row-wise")
         rows = int(input("enter the row size"))
         col = int(input("enter the column size"))
         print("enter elements for first matrix")
         arr= []
         for i in range(rows):
             row = []
             for j in range(col):
                 row.append(int(input()))
             arr.append(row)
         for i in range(rows):
            c=0
            for j in arr[i]:
               prime=1
               if j<2:
                  prime=0
               else:
                  for k in range(2,int(math.sqrt(j))+1):
                     if j%k==0:
                        prime=0
                        break
                  if prime==1:
                     c+=1
               print("Row", i + 1, "Prime Count =", c)         
      case 2:
         print("Count Prime Numbers Row-wise")
         rows = int(input("enter the row size"))
         col = int(input("enter the column size"))
         print("enter elements for first matrix")
         arr= []
         for i in range(rows):
             row = []
             for j in range(col):
                 row.append(int(input()))
             arr.append(row)
         for i in range(col):
            count=0
            for j in range(rows):
               n=arr[j][i]
               if n>1:
                  sum=0
                  for k in range(1,(n//2)+1):
                     if n % k == 0:
                        sum += k
                  if sum == n:
                        count += 1
            print(f"Column {i+1} Perfect Number Count = {count}")
      case 3:
         print("Display Row-wise Sum")
         rows = int(input("enter the row size"))
         col = int(input("enter the column size"))
         print("enter elements for first matrix")
         arr= []
         for i in range(rows):
             row = []
             for j in range(col):
                 row.append(int(input()))
             arr.append(row)
             c=0
             for i in range(rows):
                for j in range(col):
                  c=c+arr[i][j]
             print("Row ",i +1,"Sum =",c)   
      case 4:
          print("Thank You for Using Matrix Operations Management System")
          break
      case _:
          print("Invalid Choice") 
