# def hello(name,age):
#     print("name is ",name,"and age is ",age)
# hello("abc",30)#name is  abc and age is  30

# def hello(name,age):
#     print("name is ",name,"and age is ",age)
# print(30,"abc")#30 abc


# def hello(name,int(age)):
#     print("name is ",name,"and age is ",age)
# print("abc",30)#error

# def hello(name,age):
#     print("name is ",name,"and age is ",age)
# hello(age=30,name="deepika")#name is  deepika and age is  30
# #hello(age1=30,name="deepika")#error


# def hello(name,age):
#     print("name is ",name,"and age is ",age)
# hello("deepika",age=30)#name is  deepika and age is  30
# hello(age=30,"deepika")#error


# def hello(age,name):
#     print("name is ",name,"and age is ",age)
# hello(age=30,"deepika")#SyntaxError: positional argument follows keyword argument



# def hello(name,age,address):
#     print("name is ",name,"and age is ",age,address)
# hello("deepika",age=30,address="chennai")#name is  deepika and age is  30 chennai



# def hello(name,age=18):
#     print("name is ",name,"and age is ",age)
# hello("deepika")#name is  deepika and age is  18
# hello("deepika",40)#name is  deepika and age is  40


# def hello(name,age=18,address="india"):
#     print("name is ",name,"and age is ",age,"and address",address)
# hello("deep")
# hello("kat",40)
# hello("abc",40,"hyd")

# # name is  deep and age is  18 and address india
# # name is  kat and age is  40 and address india
# # name is  abc and age is  40 and address hyd


# def hello(age=18,address="india",name):
#     print("name is ",name,"and age is ",age,"and address",address)
# hello("deep")#SyntaxError: parameter without a default follows parameter with a default


# def functionname(*args):
#     body

# def showno(*args):
#     print(args)
# showno(1,2,3,4,5,5)#(1, 2, 3, 4, 5, 5)

# def show(*a):
#     print(a)
# show(1)#(1,)
# show()#()


# #WAP TO PERFORM SUM OF UNLIMITED NO.
# def add(*a):
#     total=0
#     for num in a:
#         total=total+num
#     return total
# print(add(10,20))#30
# print(add(10,20,40,50,60))#180

# def display(name,*m):
#     print(name)
#     print(m)

# display("deep",10,20,30)#deep
# #(10, 20, 30)

# #WAP TO FIND AVG. OF ANY NO'S
# def avg (*a):
#     return sum(a)/len(a)
# print(avg(2,3+4j,))#(2.5+2j)


# num=[10,20,30,40]
# def add(a,b,c,d):
#     return a+b+c+d
# print(add(*num))#100


# num=[10,20,30,40,50]
# def add(a,b,c,d):
#     return a+b+c+d
# print(add(*num))#TypeError: add() takes 4 positional arguments but 5 were given


# def add(*a):
#     return sum(a)

# print(add([10,20,30]))
# #TypeError: unsupported operand type(s) for +: 'int' and 'list'

# def add(*a):
#     return sum(a)

# print(add(*[10,20,30]))#60


# def add(*a):
#     return sum(a)

# print(add((10,20,30)))#TypeError: unsupported operand type(s) for +: 'int' and 'tuple'

# def show(**kwarg):
#     print(kwarg)
# show(name="abc",age=30,add="indore")
# #{'name': 'abc', 'age': 30, 'add': 'indore'}


# def show(**kwarg):
#     for k,v in kwarg.items():
#         print(k,"and",v)
# show(name="abc",age=30,add="indore")
# # name and abc
# # age and 30
# # add and indore

# def display(name,**details):
#     print("name is ",name)
#     print("details",details)
#     for k,v in details.items():
#         print(k,"and",v)

# display(name="abc",age=30,add="indore")

# # name is  abc
# # details {'age': 30, 'add': 'indore'}
# # age and 30
# # add and indore


def Create(**info):
    if "name" in info:
        print("welcome",info["name"])
    if "email" in info:
        print("email",info["email"])
Create(name="abc",email="abc@gmail.com")
# welcome abc
# email abc@gmail.com
