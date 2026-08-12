'''a=[1,2,[3,4,[5,6]]]
print(a)
print(a[2])
print(a[2][0])
print(a[2][2])
print(a[2][2][1])


a=[
  [
    [1,2],
    [3,4]
  ],
  [
    [6,7],
    [8,9]
  ]
      
]
print(a)
t=(1,2,3)
print(t)
print(type(t))


t=1,2,3
print(t)
print(type(t))

t=()
print(t)
print(type(t))


t=(10)
print(t)
print(type(t))#o==int


t=("h")
print(t)
print(type(t))#o==int


t=tuple([10,20])
print(t)
print(type(t))

t=(10,20)
print(t[0])
print(t[-1])
print(t[1:3])


t=(10,20)
t[0]=900
print(t[0])
'''

t=([10],20)
t[0].append(900)
print(t[0])


a,b,c,d=(10,20,3,4)
print(a)
print(b)
print(c)
print(d)


a,*b=(10,20,3,4)
print(a)
print(b)


a,*b,c=(10,20,3,4,8)
print(a)
print(b)
print(c)


t=(10,20,20,20)
print(t.count(20))
print(len(t))
print(max(t))
print(min(t))
print(sum(t))


t=(10,20)
for i in t:
    print(i)


t=(10,20)
for i in range(len(t)):
    print(t[i])

t=(10,30)
print(t*3)

t=((10,20),(20,30,40))
print(t)
print(t[0])
print(t[0][1])

t=(10,20)
t1=(10,20)
print(id(t))
print(id(t1))


t=[10,20]
t1=[10,20]
print(id(t))
print(id(t1))


#WAP to read employe details from user and store them as a tuple
id=int(input("enter id "))
name=input("name")
dept=input("dept")
sal=int(input("enter salary"))
employe=(id,name,dept,sal)
print("employe details")
print("id is",employe[0])
print("name is",employe[1])
print("dept is",employe[2])
print("sal",employe[3])
#error == employe[1]="dipu"




#WAP to read product details like product name ,price , and quantity
#in tuple() and cal total bill

pname=input("pname")
p=float(input("price"))
qty=int(input("qty"))
bill=(pname,p,qty)
amount=bill[1]*bill[2]
print("bill details")
print(bill[0],"->")
print("price is",bill[1])
print("total amount",amount)


