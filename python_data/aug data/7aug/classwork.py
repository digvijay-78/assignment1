'''a=[[10,20],[30,40]]
a[1][0]=100
print(a)
a[0]=[9,9]
print(a)

a.append([8,9])
print(a)

a[0].append(11)
print(a)

#a[0].remove(10)
#print(a) error

a=[[1,2],[30,40]]
a.pop(1)

#matrix
a=[
    [1,2],
    [3,4]
]
print(a)

a=[
    [1,2,3],
    [3,4,8],
    [9,10,11]
]
print(a)
print(a[0][0])
print(a[0][1])
print(a[0][2])
print(a[1][0])



#WAP to print a matix elemnts row wise
a=[
    [1,2,3],
    [3,4,8],
    [9,10,11]
]
for i in a:
    print(*i)


#WAP to print elements of the matrix
a=[
    [1,2,3],
    [3,4,8],
    [9,10,11]
]
for row in a:
    for value in row:
        print(value,end=" ")
    print()


#WAP to print only even elements from a matrixs

a=[
    [1,2,3],
    [3,4,8],
    [9,10,11]
]
for i in a:
    for value in i:
        if value%2==0:
            print(value)


#wap to read rows and columns from user and read elemnts from user and display them
row =int(input("enter the row size"))
col =int(input("enter the column size"))
matrix=[]
for i in range(row):
    row=[]
    for j in range(col):
        row.append(int(input()))
    matrix.append(row)
print("matrix elemts are")

for row in matrix:
    for value in row:
        print(value,end=" ")
    print()

'''
#wap sum of matrix elemnt
row =int(input("enter the row size"))
col =int(input("enter the column size"))
matrix=[]
s=0
for i in range(row):
    row=[]
    for j in range(col):
        row.append(int(input()))
    matrix.append(row)
print("matrix elemts are")

for row in matrix:
    for value in row:
        s=s+value
print(s)