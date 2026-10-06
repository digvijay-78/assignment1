"""8.
MATRIX PATTERN DETECTION SYSTEM

A satellite monitoring center stores signal strengths in matrix form.
Engineers want to identify special patterns in the matrix.

Menu
1. Count Even Numbers Above Main Diagonal
2. Count Odd Numbers Below Main Diagonal
3. Display Boundary Elements
4. Exit
Requirements
Choice 1 – Count Even Numbers Above Main Diagonal

Count all even numbers where:

column > row
Choice 2 – Count Odd Numbers Below Main Diagonal

Count all odd numbers where:

row > column
Choice 3 – Display Boundary Elements

Display all elements present on:

First Row
Last Row
First Column
Last Column

without repeating corner elements.

Sample Input
1 2 3
4 5 6
7 8 9
Output
Even Numbers Above Main Diagonal = 2
(2, 6)

Odd Numbers Below Main Diagonal = 1
(7)

Boundary Elements:
1 2 3 6 9 8 7 4"""
print("MATRIX PATTERN DETECTION SYSTEM")
while True:
    print("\n1. Count Even Numbers Above Main Diagonal")
    print("2. Count Odd Numbers below the main diagonal")
    print("3. display boundary elements ")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            m
        case 2:
            m= []
            row = int(input("Enter the no. of rows: "))
            col = int(input("Enter the no. of columns: "))
            for i in range(row):
                rows=[]
                for j in range(col):
                    rows.append(int(input(f"Enter the element of [{i},{j}]: ")))
                m.append(rows)
            print(m)
            c=[]
            for i in range(row):
                for j in range(col):
                    if j<i:
                        if m[i][j]%2!=0:
                            c.append(m[i][j])
            print("\ncount of odd number below main diagonal: ", len(c),"\n",c)
        case 3:
            matrix= []
            row = int(input("Enter the no. of rows: "))
            col = int(input("Enter the no. of columns: "))
            for i in range(row):
                rows=[]
                for j in range(col):
                    rows.append(int(input(f"Enter the element of [{i},{j}]: ")))
                matrix.append(rows)
            print(matrix)
            for j in range(col):
                print(matrix[0][j], end=" ")
            for i in range(1,row):
                print(matrix[i][col-1], end=" ")
            for j in range(col-2,-1,-1):
                print(matrix[row-1][j], end = " ")
            for i in range(row-2, 0, -1):
                print(matrix[i][0], end=" ")
        case 4:
            print("Exit!!!!")
            break



# m=[[1,2,3],[4,5,6],[7,8,9]]
# c=[]
# for i in range(len(m)):
    # for j in range(len(m)):
        # if j>i:
            # if m[i][j]%2==0:
                # c.append(m[i][j])