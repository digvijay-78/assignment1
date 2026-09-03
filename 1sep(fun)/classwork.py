# def bill (**items):
#     t=0
#     for item ,price in items.items():
#         t+=price
#     return t

# print(bill(shirt=500,jens=1000,sho=2000))#3500

# def hello(name,age):
#     print(name,age)
# hello("deep",30)#*positional
# hello(name="deep",age=30)#*key word


# def hello(name,age,/):
#     print(name,age)
# hello(name="deep",age=30)
# #*TypeError: hello() got some positional-only arguments passed as keyword arguments: 'name, age'


# def funname(para1,para2,/):
#     pass

# def funname(para1,*,para2):
#     pass

# def hello(name,*,city):
#     print(name,city)

# #hello("deep","ch")error
# hello("deep",city="ch")#*deep ch

# def payment(id,name,/,amo,method,*,currency,tax):
#     print(id,name,amo,method,currency,tax)
# payment(101,"abc",5000,"upi",currency="INR",tax=6)
# payment(101,"abc",amo=5000,method="upi",currency="INR",tax=7)

# lambda arguments:expression

# def squ(x):
#     return x*x
# print(squ(5))

# sq=lambda x: x*x
# print(sq(5))

# def add(a,b):
#     return a+b
# print(add(10,20))

# add=lambda a,b:a+b
# print(add(10,20))

# #?WAf to find greatest of 2 no.s using lambda expression
# max=lambda a,b : a if a>b else b
# print(max(10,20))

# map(function,iterable1,2,3,......)

# n=[1,2,3,4,5,6]
# def sq(n):
#     return n*n
# res=map(sq,n)
# print(list(res))#[1, 4, 9, 16, 25, 36]

# n=[1,2,3,4,5,6]
# res=map(lambda x:x*x,n)
# print(list(res))#[1, 4, 9, 16, 25, 36]

# name=["gopal","prince","digvijay"]
# def change(x):
#     return x.upper()
# res=map(change,name)
# print(list(res))#['GOPAL', 'PRINCE', 'DIGVIJAY']

# res=map(lambda x:x.upper(),name)
# print(list(res))#['GOPAL', 'PRINCE', 'DIGVIJAY']
# res=list(map(lambda x:x.upper(),name))
# print(res)#['GOPAL', 'PRINCE', 'DIGVIJAY']

# #WAP to capitalize every word of a list
# name=["gopal","prince","digvijay"]
# def cap(x):
#     return x.capitalize()
# res=(map(cap,name))
# print(list(res))#['Gopal', 'Prince', 'Digvijay']


# #WAP to find len every word of a list
# name=["gopal","prince","digvijay"]
# def l(x):
#     return len(x)
# res=(map(l,name))
# print(list(res))#[5, 6, 8]


# #WAP to find len every word of a list
# name=["gopal","prince","digvijay"]
# res=list(map(lambda x:len(x),name))
# print(res)#[5, 6, 8]



#WAP to add 2 list elements 
n=[1,2,3,4,]
m=[6,7,8,9]
def add(a,b):
    return a+b
res=list(map(add,n,m))
print(res)
#note jitne element comon hai utne hee karega 


# n=[1,2,3,4,]
# m=[6,7,8,9]
# res=list(map(lambda a,b:a+b,n,m))
# print(res)

#WAP to take list of integers and print even or odd
n= [1,2,3,4,5,6]
def eo(x):
    if x%2==0:
        return "even"
    else:
        return "odd"
res=list(map(eo,n))
print(res)#['odd', 'even', 'odd', 'even', 'odd', 'even']

res=list(map(lambda x:"even" if x%2==0 else "odd",n))
print(res)

#WAP TO CONVERT NO. OF LIST INTO STRING
n=[1,2,3,4,5,6]
res=list(map(lambda x:str(x),n))
print(res)#['1', '2', '3', '4', '5', '6']

#WAP to calulate student grades
n=[90,77,33,100]
def cal(x):
    if x>80:
        return "A"
    elif x>70:
        return "B"
    else:
        return "C"
res=list(map(cal,n))
print(res)
res=list(map(lambda x: "A" if x>80  else "B" if x>70 else "C",n))
print(res)#['A', 'B', 'C', 'A']