# class student :
#     college ="iit"
#     def __init__ (self,name):
#         self.name=name
# s1=student("deep")
# s1.college="NIT"
# print(s1.__dict__)#{'name': 'deep', 'college': 'NIT'}
# print(student.__dict__)
# """{'__module__': '__main__', '__firstlineno__': 1, 'college': 'iit',
# '__init__': <function student.__init__ at 0x0000016EAA153A60>, 
# '__static_attributes__': ('name',), '__dict__': <attribute '__dict__'of 'student' objects>, 
# '__weakref__': <attribute '__weakref__' of 'student' objects>, '__doc__': None}"""


# class student :
#     college ="iit"
#     def __init__ (self,name):
#         self.name=name
#         student.city="indore"
#     def m1(self):
#         student.marks=90
# s1=student("deep")
# student.contact=939921
# print(s1.__dict__)#{'name': 'deep'}
# s1.m1()
# print(student.__dict__)
# """{'__module__': '__main__', '__firstlineno__': 15, 'college': 'iit', '__init__': 
# <function student.__init__ at 0x00000205626A3A60>, 'm1': <function student.m1 at 0x00000205626AC860>, 
# '__static_attributes__': ('name',), '__dict__': <attribute '__dict__' of 'student' objects>, '__weakref__': 
# <attribute '__weakref__' of 'student' objects>, '__doc__': None, 'city': 'indore', 'contact': 939921, 'marks': 90}"""

# class test:
#     a=10
#     def __init__(self) :
#         self.b=20
# t1=test()
# t2=test()
# t2.a+=1
# print(t2.a)#11
# print(test.a)#10
# print(t1.a)#10


# class test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#         self.c=30
#         self.d=40
# t1=test()
# t2=test()
# print(t1.__dict__)#{'a': 10, 'b': 20, 'c': 30, 'd': 40}
# del t1.c
# del t1.d
# print(t1.__dict__)#{'a': 10, 'b': 20}

# class student :
#     def display(self):
#         self.a=10
#         print("hello")
# s1=student()
# s1.display()#kese hota hai -> student.display(s1)




# class student :
#     def display(self,name):
#         self.name=name#setter mutator
#     def getname(self):
#         return self.name

# s1=student()
# s1.display("deep")
# print(s1.getname())#deep


# class student:
#     college="iit"
#     def __init__(self,name) :
#         self.name=name
#     @classmethod
#     def change_college(cls,new):
#         cls.college=new
# s1=student("abc")
# print(s1.name)
# print(s1.college)
# student.change_college("NIT")
# print(s1.name)
# print(s1.college)
# """abc
# iit
# abc
# NIT"""

# class student:
#     college="iit"
#     def __init__(self,name) :
#         self.name=name
#     @classmethod
#     def change_college(cls,new):
#         cls.college=new
# s1=student("abc")
# print(s1.name)
# print(s1.college)
# student.change_college("NIT")
# print(s1.name)
# print(s1.college)
# s1.change_college("skit")
# print(student.college)
# """abc
# iit
# abc
# NIT
# skit"""

# class calculator:
#     @staticmethod
#     def add(a,b):
#         return a+b
# print(calculator.add(10,20))#30

# class calculator:
#     @staticmethod
#     def add(a,b):
#         return a+b
# c=calculator()
# print(calculator.add(10,20))#30
# print(c.add(20,30))#50
# print(c.__dict__)#{}

# class calculator:
#     @staticmethod
#     def add(self,a,b):
#         return a+b
# c=calculator()
# print(calculator.add(10,20))#TypeError: calculator.add() missing 1 required positional argument: 'b'

# class calculator:
#     college="iit"
#     @staticmethod
#     def add(a,b):
#         print(calculator.college)
#         return a+b
# print(calculator.add(10,20))#iit,30


# class emp:
#     company="tcs"
#     def instance_method(self):
#         print("instance")
#     @classmethod
#     def class_method(cls):
#         print(cls.company)
#     @staticmethod
#     def hello():
#         print("static method")
# c1=emp()
# emp.class_method()
# emp.hello()
# c1.instance_method()
# """tcs
# static method
# instance"""



# class emp:
#     def __init__(self,name):
#         self.name=name
#     @staticmethod
#     def hello():
#         print(self.name)
# c1=emp("deep")
# emp.hello()#NameError: name 'self' is not defined


# class emp:
#     def __init__(self,name):
#         self.name=name
#     @staticmethod
#     def hello():
#         print(c1.name)
# c1=emp("deep")
# emp.hello()#deep


# class emp:
#     def __init__(self,name):
#         self.name=name
#     @staticmethod
#     def hello(self):
#         print(self.name)
# c1=emp("deep")
# emp.hello(c1)#deep

# class emp:
#     def __init__(self,name):
#         self.name=name
#     @staticmethod
#     def hello():
#         print(c1.name)
# c1=emp("deep")
# emp.hello()#deep


# class emp:
#     def __init__(self,name):
#         self.name=name
#     @staticmethod
#     def hello(self):
#         print(self.name)
# c1=emp("deep")
# emp.hello()#TypeError: emp.hello() missing 1 required positional argument: 'self'
