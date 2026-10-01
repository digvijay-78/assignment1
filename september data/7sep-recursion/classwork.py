# #WAP to find factorial of no. using recursion
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     return n*fact(n-1)
# print(fact(5))

# #wAP to find power function using recursion
# def pow (b,e):
#     if e==0:
#         return 1
#     return b*pow(b,e-1)
# print(pow(2,4))

# #WAP to count digits in a no.
# def count(n):
#     if n==0:
#         return 0
#     return 1+count(n//10)
# print(count(0.245))

# def hello(name):
#     def message():
#         return "welcome"
#     print("hello",name)
#     print(message())
# hello("deep")
# #hello deep
# #welcome


# def hello(name):
#     def message():
#         return "welcome"
#     print("hello",name)
#     print(message())
# hello("deep")
# #message () error we cant call inner fun from outside 

# def outer ():
#     x=10
#     def inner ():
#         print("value of x is ",x)
#     inner()
# outer()#value of x is  10


# def outer ():
#     x=10
#     def inner ():
#         y=20
#         print("value of x is ",x)
#     inner()
#     print("value of y is ",y)
# outer()#NameError: name 'y' is not defined


# def outer ():
#     x=10
#     def inner ():
#         x=20
#         print("value of x is ",x)
#     inner()
#     print("value of y is ",x)
# outer()#value of x is  20
# #value of y is  10



# def outer ():
#     x=10
#     def inner ():
#         nonlocal x
#         x=100
#         print("value of x is ",x)
#     inner()
#     print("value of x is ",x)
# outer()
# #value of x is  100
# #value of x is  100

# x=100
# def outer ():
#     x=10
#     print("inside  x is ",x)
# outer()
# print("outside x is ",x)
# # inside  x is  10
# # outside x is  100


# x=100
# def outer ():
#     x=10
#     def inner():

#         print("inside  x is ",x)
#     inner()
# outer()
# print("outside x is ",x)

# #L=> local scope
# #E =>enclosing
# #G => global
# #B => built in scope 


# x=100
# def outer ():
#     def inner():
#         print("inside  x is ",x)
#         print("len",len([1,2,3,4,5]))
#     inner()
# outer()
# print("outside x is ",x)

# # inside  x is  100
# # len 5
# # outside x is  100


# def calculatetotal(price,taxrate):
#     def caltax():
#         return price*taxrate
#     return price+caltax()
# print(calculatetotal(1000,0.18))#1180.0


# def billgenrate(amount):
#     def applydiscount():
#         if amount>10000:
#             return amount*0.10
#         return 0
#     discount=applydiscount()
#     final=amount-discount
#     return final
# print(billgenrate(15000))#13500.0


