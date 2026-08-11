'''1.
=========================================================
        MATRIX OPERATIONS MANAGEMENT SYSTEM
=========================================================


A data analysis company stores numerical information in matrix form.
To help employees perform matrix-related operations efficiently,
the company wants a menu-driven application.

The application should allow the user to:

1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

The user must enter the number of rows, columns, and all matrix
elements. The program should perform the selected operation and
display the result.

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user chooses Exit.

   1. Add Two Matrices
   2. Subtract Two Matrices
   3. Compare Two Matrices
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all elements of Matrix A and Matrix B from the user whenever
   required.

4. Based on the user's choice:

   Choice 1 - Add Two Matrices
   --------------------------------
   Add corresponding elements of both matrices and display
   the resultant matrix.

5. Choice 2 - Subtract Two Matrices
   --------------------------------
   Subtract corresponding elements of Matrix B from Matrix A
   and display the resultant matrix.

6. Choice 3 - Compare Two Matrices
   --------------------------------
   Check whether both matrices are equal.

   Two matrices are considered equal if:
   - They have the same dimensions.
   - Corresponding elements are equal.

   Display:
   "Matrices are Equal"
   or
   "Matrices are Not Equal"

7. Choice 4 - Exit
   --------------------------------
   Display:
   "Thank You for Using Matrix Operations Management System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

Enter your choice: 1

Enter number of rows: 2
Enter number of columns: 2

Enter Matrix A:
1 2
3 4

Enter Matrix B:
5 6
7 8

Result Matrix:
6 8
10 12

---------------------------------------------------------

Menu
1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

Enter your choice: 3

Enter number of rows: 2
Enter number of columns: 2

Enter Matrix A:
1 2
3 4

Enter Matrix B:
1 2
3 4

Output:
Matrices are Equal

---------------------------------------------------------

Menu
1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

Enter your choice: 4

Output:
Thank You for Using Matrix Operations Management System

========================================================='''
print("WELCOME MATRIX OPERATIONS MANAGEMENT SYSTEM")


while True:
    print("-"*32)
    print("MENU")
    print('''1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit''')
    a = int(input("ENTER YOUR CHOICE"))

    match a:
        case 1:
            rows = int(input("enter the row size"))
            col = int(input("enter the column size"))
            print("enter elements for first matrix")
            A = []
            for i in range(rows):
                row = []
                for j in range(col):
                    row.append(int(input()))
                A.append(row)
            print("enter elements for sec matrix")
            B = []
            for i in range(rows):
                row = []
                for j in range(col):
                    row.append(int(input()))
                B.append(row)
            c = []
            for i in range(len(A)):
                row = []
                for j in range(len(A[i])):
                    row.append(A[i][j] + B[i][j])
                c.append(row)
            print("display")
            for row in c:
                print(*row)

        case 2:
            rows = int(input("enter the row size"))
            col = int(input("enter the column size"))
            print("enter elements for first matrix")
            A = []
            for i in range(rows):
                row = []
                for j in range(col):
                    row.append(int(input()))
                A.append(row)
            print("enter elements for sec matrix")
            B = []
            for i in range(rows):
                row = []
                for j in range(col):
                    row.append(int(input()))
                B.append(row)
            c = []
            for i in range(len(A)):
                row = []
                for j in range(len(A[i])):
                    row.append(A[i][j] - B[i][j])
                c.append(row)
            print("display")
            for row in c:
                print(*row)

        case 3:
            rows = int(input("enter the row size"))
            col = int(input("enter the column size"))

            print("enter elements for first matrix")
            A = []
            for i in range(rows):
                row = []
                for j in range(col):
                    row.append(int(input()))
                A.append(row)

            print("enter elements for sec matrix")
            B = []
            for i in range(rows):
                row = []
                for j in range(col):
                    row.append(int(input()))
                B.append(row)

            c =0
            for i in range(len(A)):
                for j in range(len(A[i])):
                    if A[i][j] == B[i][j]:
                        c+=1
            if c==rows*col:                
               print("equal")
            else:
                print("not equal")
        case 4:
            print("Thank You for Using Matrix Operations Management System")
            break
        case _:
            print("Invalid Choice") 
