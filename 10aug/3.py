'''3.

=========================================================
         MATRIX QUALITY CHECK SYSTEM
=========================================================
Scenario
A manufacturing company records quality inspection values in
matrix form. The Quality Control team wants a menu-driven
application to analyze the inspection data and generate reports.

The application should allow the user to:

1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Count Armstrong Numbers Row-wise
   2. Count Palindrome Numbers Column-wise
   3. Display Average of Each Row
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Count Armstrong Numbers Row-wise
   -------------------------------------------
   Count and display the number of Armstrong numbers
   present in each row.

   Examples:
   153, 370, 371, 407

5. Choice 2 - Count Palindrome Numbers Column-wise
   -----------------------------------------------
   Count and display the number of palindrome numbers
   present in each column.

   Examples:
   121, 131, 444, 1221

6. Choice 3 - Display Average of Each Row
   --------------------------------------
   Calculate and display the average of each row.

7. Choice 4 - Exit
   --------------------------------------
   Display:
   "Thank You for Using Matrix Quality Check System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit

Enter your choice: 1

Enter rows: 3
Enter columns: 3

Enter matrix elements:
153 121 10
370 22 44
407 15 131

Output:
Row 1 Armstrong Count = 1
Row 2 Armstrong Count = 1
Row 3 Armstrong Count = 1

---------------------------------------------------------

Enter your choice: 2

Output:
Column 1 Palindrome Count = 0
Column 2 Palindrome Count = 3
Column 3 Palindrome Count = 2
'''
print("MATRIX QUALITY CHECK SYSTEM")
while True:
   print("-"*32)
   print("MENU")
   print('''1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit''')
   a=int(input("ENTER YOUR CHOICE"))

   match a:
      case 1:
         print("Count Armstrong Numbers Row-wise")
         rows = int(input("enter the row size"))
         col = int(input("enter the column size"))
         print("enter elements for matrix")
         arr= []
         for i in range(rows):
             row = []
             for j in range(col):
                 row.append(int(input()))
             arr.append(row)
         for wors in arr:
            print(*wors)

         for i in range(rows) :
            count=0
            for j in range(col):
               l=len(str(arr[i][j]))
               z=arr[i][j]
               temp=z
               s=0
               while z>0:

                d=z%10
                s=s+d**l
                z=z//10
               if s == temp:
                count += 1

            print("Row", i+1, "Armstrong Count =", count)
      case 2:
         print("Count Palindrome Numbers Column-wise")
         rows = int(input("enter the row size"))
         col = int(input("enter the column size"))
         print("enter elements for matrix")
         arr= []
         for i in range(rows):
             row = []
             for j in range(col):
                 row.append(int(input()))
             arr.append(row)
         for wors in arr:
            print(*wors)

         for i in range(col):
            count=0
            for j in range(rows):
               x=str(arr[j][i])
               temp=x[::-1]

               if x==temp:
                  count+=1
            print("Column", i + 1, "Palindrome Count =", count)
      case 3:
         print("Display Average of Each Row")
         rows = int(input("enter the row size"))
         col = int(input("enter the column size"))
         print("enter elements for matrix")
         arr= []
         for i in range(rows):
             row = []
             for j in range(col):
                 row.append(int(input()))
             arr.append(row)
         for wors in arr:
            print(*wors)
         for i in range(rows):
            s=0
            for j in range(col):
               s=s+arr[i][j]
            s=s/col
            print("ROW",i+1,"AVG.=",s)
      case 4:
            print("Thank You for Using Matrix Quality Check System")
            break
      case _:
            print("Invalid Choice") 
