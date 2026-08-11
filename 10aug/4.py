'''4.

=========================================================
        MATRIX DIAGONAL ANALYSIS SYSTEM
=========================================================

Scenario

A security company stores surveillance data in matrix form.
The analyst wants a menu-driven application to examine the
diagonal elements of the matrix and generate reports.

The application should allow the user to:

1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Display Main Diagonal Elements
   2. Display Secondary Diagonal Elements
   3. Compare Main and Secondary Diagonal Sums
   4. Exit

2. Read the size of a square matrix from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Display Main Diagonal Elements
   -----------------------------------------
   Display all elements present in the main diagonal.

5. Choice 2 - Display Secondary Diagonal Elements
   ----------------------------------------------
   Display all elements present in the secondary diagonal.

6. Choice 3 - Compare Main and Secondary Diagonal Sums
   ---------------------------------------------------
   Calculate the sum of both diagonals and display:

   - Main Diagonal Sum
   - Secondary Diagonal Sum
   - Which diagonal has the greater sum
   - Or whether both sums are equal

7. Choice 4 - Exit
   -----------------------------------------
   Display:
   "Thank You for Using Matrix Diagonal Analysis System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Enter size of matrix: 3

Enter matrix elements:

1 2 3
4 5 6
7 8 9

Menu
1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

Enter your choice: 1

Output:
Main Diagonal Elements:
1 5 9

---------------------------------------------------------

Enter your choice: 2

Output:
Secondary Diagonal Elements:
3 5 7

---------------------------------------------------------

Enter your choice: 3

Output:
Main Diagonal Sum = 15
Secondary Diagonal Sum = 15
Both Diagonal Sums are Equal

========================================================='''

print("MATRIX DIAGONAL ANALYSIS SYSTEM")
while True:
    print("-"*32)
    print("MENU")
    print('''1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit''')
    a = int(input("ENTER YOUR CHOICE"))

    match a:
        case 1:
            size=int(input("Enter size of matrix:"))
            rows =size
            col = size
            print("enter elements for  matrix")
            arr= []
            for i in range(rows):
                row = []
                for j in range(col):
                    row.append(int(input()))
                arr.append(row)
            s=[]
            for i in range(len(arr)):
                s.append(arr[i][i])
            print("Main Diagonal Elements: \n",*s)
        case 2:
            size=int(input("Enter size of matrix:"))
            rows =size
            col = size
            print("enter elements for  matrix")
            arr= []
            for i in range(rows):
                row = []
                for j in range(col):
                    row.append(int(input()))
                arr.append(row)
            for i in range(rows):
                for j in range(col):
                    s=arr[i][j-1]
                    print("Secondary Diagonal Elements:\n",s)
                    col=col-1
                    break
        case 3:
          print("======Compare Main and Secondary Diagonal Sums======")
          r1 = int(input("Enter the number of rows: "))
          c1 = int(input("Enter the number of columns: "))
          A = []
          for i in range(r1):
              row = []
              for j in range(c1):
                  row.append(int(input(f"Enter the value {i+1}: ")))
              A.append(row)
          print("Matrix is:")
          print(*A)
          main_sum = 0
          secondary_sum = 0
          for i in range(r1):
              main_sum = main_sum + A[i][i]
              secondary_sum = secondary_sum + A[i][c1 - 1 - i]
          print("Main Diagonal Sum =", main_sum)
          print("Secondary Diagonal Sum =", secondary_sum)
          if main_sum > secondary_sum:
              print("Main Diagonal has the greater sum")
          elif secondary_sum > main_sum:
              print("Secondary Diagonal has the greater sum")
          else:
              print("Both Diagonal Sums are Equal")
        case 4:
              print("\nThank You for Using Matrix Quality Check System")
              break
        case _:
            print("IVNVALID CHOICE PLEASE CHOOSE BETWEEN 1 and 4!!!")
                 