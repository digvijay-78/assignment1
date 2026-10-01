# class A:
#     def f1(self) :
#         print(" f1 of A")
# class B(A):
#     def __init__(self) :
#         super().__init__()
#         print("constructr B")  
# class C(A):
#     def __init__(self) :
#         super().__init__()
#         print("constructr C")  

# class D(B,C):
#     def __init__(self) :
#         super().__init__()
#         print("constructr D")  

# o=D()
# o.f1()
# # constructr C
# # constructr B
# # constructr D
# #  f1 of 
# o=D()

# print(D.mro())

# """constructr A
# constructr C
# constructr B
# constructr D
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]"""



# class A:
#     pass
# class B:
#     pass

# obj=B()
# print(isinstance(obj,B))#TRUE
# print(isinstance(obj,A))#FALSE

# class A:
#     pass
# class B(A):
#     pass

# obj=B()
# print(isinstance(obj,B))#TRUE
# print(isinstance(obj,A))#TRUE


# class A:
#     pass
# class B(A):
#     pass

# obj=B()
# print(issubclass(B,A))#TRUE
# print(issubclass(A,B))#FALSE

# class A:
#     def cal(self):
#         print("calculation of 8 percentage")
# class B(A):
#     def cal(self):
#         print("calculation of 7 percentage")
# obj=B()
# obj.cal()#calculation of 7 percentage


# class EMP:
#     def salary(self,basic,bonus):
#         print("total salary",basic+bonus)


# class MANAGER:
#     def salary(self,basic,bonus):
#         print("total salary",basic+bonus+5000)
# obj1=EMP()
# obj1.salary(10000,2000)
# obj1=MANAGER()
# obj1.salary(10000,2000)
# """total salary 12000
# total salary 17000"""


# class Bird:
#     def fly(self):
#         print("bird can fly")
# class Airplane:
#     def fly(self):
#         print("airplane can fly")

# objects=[Bird(),Airplane()]
# for obj in objects:
#     obj.fly()

# """bird can fly
# airplane can fly"""


# print(len("hello"))#5
# print(len([2,3,4,5,65]))#5
# print(len((2,3)))#2


# print(10+20)
# print("wel"+"come")
# print(5*3)
# print("hello"*3)
# """30
# welcome
# 15
# hellohellohello"""

# class A:
#     def hekko(self,a):
#         print("A")
#     def hekko(self,b):
#         print("B")
#     def hekko(self,c):
#         print("C")
# obj=A()
# obj.hekko(10)#C


# class A:
#     def __init__(self,a):
#         print("A")
#     def __init__(self,b):
#         print("B")
#     def __init__(self,c):
#         print("C")
# obj=A(10)#C