# class student :
#     def set(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print("data student is ",self.name,self.age)
# s1=student()
# s1.set("deepika",30)#student.set(s1,"deepika",30)
# s1.display()
# #data student is  deepika 30


# class student :
#     def set(self):
#         self.name="deep"
#         self.age=30
#     def display(self):
#         print("data student is ",self.name,self.age)
# s1=student()
# s1.set()
# s1.display()
# #data student is  deepika 30




# class student :
#     def set(self):
#         self.name="deep"
#         self.age=30
#     def display(self):
#         print("data student is ",self.name,self.age)
# s1=student()
# s1.set()
# s1.display()
# print("id od s1",id(s1))

# s2=student()
# s2.set()
# s2.display()
# print("id od s2",id(s2))

# #data student is  deep 30
# # id od s1 2050249879776
# # data student is  deep 30
# # id od s2 2050252557200

# class student :
#     def set(self,n,a):
#         self.name=n
#         self.age=a
#     def display(self):
#         print("data student is ",self.name,self.age)
# s1=student()
# s1.set("rash",30)
# s1.display()
# print("id od s1",id(s1))

# s2=student()
# s2.set("deep",80)
# s2.display()
# print("id od s2",id(s2))

# # data student is  rash 30
# # id od s1 2034201882848
# # data student is  deep 80
# # id od s2 2034205281168




# class student :
#     def set(self,n,a):
#         self.name="deep"
#         self.age="yash"
#     def display(self):
#         print("data student is ",self.name,self.age)
# s1=student()
# s1.display()#AttributeError: 'student' object has no attribute 'name'


# class student :
#     def set(this,n,a):
#         this.name=n
#         this.age=a
#     def display(this):
#         print("data student is ",this.name,this.age)
# s1=student()
# s1.set("rash",30)
# s1.display()#data student is  rash 30


# class student :
#     def set(this,n,a):
#         this.name=n
#         this.age=a
#     def display(katapa):
#         print("data student is ",katapa.name,katapa.age)
# s1=student()
# s1.set("rash",30)
# s1.display()#data student is  rash 30

# class sum:
#     def add(self,a,b):
#         self.a=a
#         self.b=b
#         self.c=self.a+self.b
#     def display(self):
#         return self.c
# x1=sum()
# x1.add(30,40)
# v=x1.display()
# print("sum is ",v)
# #sum is  70

# class sum:
#     def add(self,a,b):
#         self.a=a

#         self.b=b
#         c=self.a+self.b
#     def display(self):
#         return self.c
# x1=sum()
# x1.add(30,40)
# v=x1.display()
# print("sum is ",v)
# #AttributeError: 'sum' object has no attribute 'c'


# class sum:
#     def add(self,a,b):
#         self.a=a

#         self.b=b
#         c=self.a+self.b
#     def display(self):
#         return c
# x1=sum()
# x1.add(30,40)
# v=x1.display()
# print("sum is ",v)
# #NameError: name 'c' is not defined



# class sum:
#     def add(self,a,b):
#         self.a=a

#         self.b=b
#         c=self.a+self.b
#         return c
# x1=sum()
# print(x1.add(30,40))#70


# class Mul:
#     def accept(self,x,y):
#         self.x=x
#         self.y=y
#     def operation(self):
#         self.z=self.x*self.y
#     def show(self):
#         print("result is :",self.z)
# obj1=Mul()
# obj1.accept(10,20)
# obj1.operation()
# obj1.show()

# #result is : 200


# class student:
#     def __init__(self):
#         print("constructor called automatically")
#     def display(self):
#         print("this is display method")
# s1=student()#constructor called automatically

# class student:
#     def __init__(self):
#         print("constructor called automatically")
#     def display(self):
#         print("this is display method")
# s1=student()#constructor called automatically
# s1.display()#this is display method


