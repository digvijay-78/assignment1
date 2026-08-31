#WAP to rotate elements
#[10,20,30]=[30,10,20]
'''
n=int(input("enter size"))
arr=[]
i=0
while i<n:
    arr.append(int(input()))
    i=i+1
last=arr[-1]
i=n-1
while i>0:
    arr[i]=arr[i-1]
    i=i-1
arr[0]=last
print(arr)
'''
#WAP count pair with given sum
#arr[1,5,7,1]=out ==2
#arr[0]+arr[1]=1+5
#arr[1]+arr[3]=5+1
'''
n=int(input("enter size"))
k=int(input("enter target sum"))
arr=[]
print("enter array elements:")
for i in range(n):
    arr.append(int(input()))
count=0
for i in range(n):
    for j in range(i+1,n):
        if arr[i]+arr[j]==k:
            count+=1

print("no. of counts",count)
'''

#list comprihension in py 
#[expression for item in iterable]
a=[1,2,3,4,5]
b=[i*3 for i in a]
#for i in a:
#   b.append(i*3)
print(b)

#conditional statements
#[expression for item in iterable if condition]
a=[1,2,3,4,5,6]
r=[val for val in a if val%2==0]
print(r)

#WAP element even and greater than 3 and square of value
a=[1,2,3,4,5,6]
r=[val*val for val in a if val>3 and val%2==0]
print(r)

#if else in list comp.
a=[1,2,3,4,5,6]
r=["even" if x%2==0 else "odd" for x in a]
print(r)

a=["java","py","react"]
r=[len(w) for w in a]
print(r)

a=["java","py","react"]
r=[w.upper() for w in a]
print(r)

a=["java","py","react"]
r=[w for w in a if len(w)>3]
print(r)

a=[1,2,3,4,5,6]
r=[x*10 if x%2==0 else x*20 for x in a]
print(r)

#nested list 
a=[1,2,[3,4],5]
print(a)

a=[[1,2],[3,4],[5,5]]
#print(a[2][1])
print(a)
print("elements row wise")
for r in a:
    print(r)

for i in a:
    for j in i:
        print(j,end=" ")
    print()


#traversing list using index in list
a=[[1,2],[3,4],[5,5]]
print(a)
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=" ")
    print()

#updating elements 
l=[1,2,3]
print(id(l))
l[1]=100
print(id(l))


a=[[1,2],[3,4],[5,5]]
print(a)
for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][0]=100
        print(a[i][j],end=" ")
    print()



