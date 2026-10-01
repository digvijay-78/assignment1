# def display(fun):
#     return fun("hello")
# def upper(value):
#     return value.upper()

# print(display(upper))#HELLO


# def display(fun,x):
#     return fun(x)
# def sq(n):
#     return n*n

# print(display(sq,5))#25 

# def display(name):
#     message=f"hello {name}"

#     def displaymessage():
#         print(message)
#     return displaymessage
# ref=display("deep")
# ref()#hello deep


# def counter():
#     count=0
#     def increment():
#         nonlocal count
#         count=count+1
#         return count
#     return increment
# #closure
# c=counter()
# print(c())#1
# print(c())#2
# print(c())#3


# def multi(x):
#     def cal(y):
#         return y*x
#     return cal
# c=multi(2)
# print(c(5))#10


# def multi(x):
#     def cal(y):
#         return y*x
#     return cal
# d=multi(2)
# c=multi(3)
# print(d(5))#10
# print(c(5))#15


# def mydecorator(fun):
#     def wrapper():
#         print("====befor calling the function====")
#         fun()
#         print("====after calling the function====")
#     return wrapper
# def display():
#     print("hello guys.........")
# design=mydecorator(display)
# design()

# # ====befor calling the function====
# # hello guys.........
# # ====after calling the function====



# def mydecorator(fun):
#     def wrapper():
#         print("====befor calling the function====")
#         fun()
#         print("====after calling the function====")
#     return wrapper
# @mydecorator
# def display():
#     print("hello guys.........")
# display()
# # ====befor calling the function====
# # hello guys.........
# # ====after calling the function====

# loggedin=True

# def loginrequired(fun):
#     def wrapper():
#         if loggedin:
#             fun()
#         else:
#             print("plz login first.....")
#     return wrapper
# @loginrequired
# def profile ():
#     print("welcome to profile")
# profile()#welcome to profile


# loggedin=False

# def loginrequired(fun):
#     def wrapper():
#         if loggedin:
#             fun()
#         else:
#             print("plz login first.....")
#     return wrapper
# @loginrequired
# def profile ():
#     print("welcome to profile")
# profile()#plz login first.....


# loggedin=True

# def loginrequired(fun):
#     def wrapper():
#         if loggedin:
#             fun()
#         else:
#             print("plz login first.....")
#     return wrapper

# def profile ():
#     print("welcome to profile")
# c=loginrequired(profile)
# c()#welcome to profile


