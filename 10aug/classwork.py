'''#WAP to find max element in list
m=[[1,3,4],[6,7,8]]
ma=m[0][0]
for row in m:
    for v in row:
        if v> ma:
            ma=v
print("max",ma)



#WAP to print main digonal sum 
m=[[1,3,4],[6,7,8],[2,5,9]]
s=0
for i in range(len(m)):
    s=s+m[i][i]
print(s)

#WAP to count even no in a matrix
m=[[1,3,4],[6,7,8],[2,5,9]]
count=0
for i in m:
    for k in i :
        if k%2==0:
            count+=1
print(count)


#WAP to search an element in matrix and display index of element

m=[[1,3,4],[6,7,8],[2,5,9]]
s=int(input("enter element you want to see"))
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j]==s:
            print("found element at index",i,j)


#WAP to add 2 matrix
a=[[2,3],[4,5]]
b=[[8,10],[9,11]]
c=[]
for i in range(len(a)):
    row=[]
    for j in range(len(a[i])):
        row.append(a[i][j]+b[i][j])
    c.append(row)
print("display")
print(*c)



#WAP to multiply 2 matrix
r1=int(input("enter rows for first matrix"))
c1=int(input("enter col for first matrix"))
print("enter elements for first matrix")
A=[]
for i in range(r1):
    row=[]
    for j in range(c1):
        row.append(int(input()))
    A.append(row)
r2=int(input("enter rows for sec matrix"))
c2=int(input("enter col for sec matrix"))
print("enter elements for sec matrix")
B=[]
for i in range(r2):
    row=[]
    for j in range(c2):
        row.append(int(input()))
    B.append(row)
if c1!=r2:
    print("multiplication not possible")
else:
    result=[]
    for i in range(r1):
        row=[]
        for j in range(c2):
            row.append(0)
        result.append(row)
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j]=result[i][j]+A[i][k]*B[k][j]
    print("result matrix is")
    # for rows in result:
    #     print(*rows)
    print(*result)








'''