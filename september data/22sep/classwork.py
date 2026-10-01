# class Parent:
#     def show(self):
#         print("this is parent method")
# class Child(Parent):
#     def show(self):
#         super().show()
#         print("this is child method")

# obj=Child()
# obj.show()
# # this is parent method
# # this is child method


# class Developer1:
#     def code1(self):
#         print("this code is from devloper1")
# class Developer2:
#     def code2(self):
#         print("this code is from developer2")
# class Tester(Developer1,Developer2):
#     def testing (self):
#         print("testing")

# obj=Tester()
# obj.code1()
# obj.code2()
# obj.testing()

# # this code is from devloper1
# # this code is from developer2
# # testing




# class Developer1:
#     def __init__(self) :
#         print("construcutor of developer1")
#     def code1(self):
#         print("this code is from devloper1")
# class Developer2:
#     def __init__(self) :
#         print("construcutor of developer2")
#     def code2(self):
#         print("this code is from developer2")
# class Tester(Developer1,Developer2):
#     def __init__(self) :
#         super().__init__()
#         print("construcutor of tester")
#     def testing (self):
#         print("testing")

# obj=Tester()
# obj.code1()
# obj.code2()
# obj.testing()

# # construcutor of developer1
# # construcutor of tester
# # this code is from devloper1
# # this code is from developer2
# # testing


# print(Tester.mro())#[<class '__main__.Tester'>, 
# #<class '__main__.Developer1'>, <class '__main__.Developer2'>, <class 'object'>]




# class Developer1:
#     def code(self):
#         print("this code is from devloper1")
# class Developer2:
#     def code(self):
#         print("this code is from developer2")
# class Tester(Developer2,Developer1):
#     pass

# obj=Tester()
# obj.code()#this code is from developer2

# class Person:
#     def __init__(self,name) :
#         self.name=name
#         print("person constructor")


# class Employee(Person):
#     def __init__(self,name,salary) :

#         Person.__init__(self,name)
#         self.salary=salary
#         print("employee constructor" )

# obj=Employee("deep",900000)

# # person constructor
# # employee constructor

# class A:
#     def show (self):
#         print("class A")
# class B:
#     def show (self):
#         print("class B")
# class C(A,B):
#     def show(self):
#         super().show()
#         super().show()
#         print("C")
# obj=C()
# obj.show()
# """class A
# class A
# C"""


# class A:
#     def show (self):
#         print("class A")
# class B(A):
#     def show1 (self):
#         print("class B")
# class C(A):
#     def show2(self):
#         print("class C")

# obj1=B()
# obj1.show()
# obj1.show1()
# #obj1.show2()#AttributeError: 'B' object has no attribute 'show2'. Did you mean: 'show'?

# obj2=C()
# obj2.show()
# obj2.show2()
# #obj2.show1()#AttributeError: 'C' object has no attribute 'show1'. Did you mean: 'show'?

# class A:
#     def fun1(self):
#         print("class A")
# class B(A):
#     def fun2 (self):
#         print("class B")
# class C(A):
#     def fun3(self):
#         print("class C")
# class D(B,C):
#     def fun4(self):
#         print("class D")

# o=D()
# o.fun1()
# o.fun2()
# o.fun3()
# o.fun4()

# class A:
#     def __init__(self) :
#         print("constructor A")
#     def fun1(self):
#         print("class A")
# class B(A):
#     def __init__(self) :
#         super().__init__()
#         print("constructor B")
#     def fun2 (self):
#         print("class B")
# class C(A):
#     def __init__(self) :
#         super().__init__()
#         print("constructor C")
#     def fun3(self):
#         print("class C")
# class D(B,C):
#     def __init__(self) :
#         super().__init__()
#         print("constructor D")
#     def fun4(self):
#         print("class D")

# o=D()

# # constructor A
# # constructor C
# # constructor B
# # constructor D

# class A:
#     def __init__(self):
#         print("constructor A")

#     def fun1(self):
#         print("class A")


# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("constructor B")

#     def fun2(self):
#         print("class B")


# class C(A):
#     def __init__(self):
#         super().__init__()
#         print("constructor C")

#     def fun3(self):
#         print("class C")


# class D(B, C):
#     def __init__(self):
#         super().__init__()
#         print("constructor D")

#     def fun4(self):
#         print("class D")


# o = D()

# o.fun1()
# o.fun2()
# o.fun3()
# o.fun4()

# # class A
# # class B
# # class C
# # class D

