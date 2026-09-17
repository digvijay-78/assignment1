# class student :
#     def __init__(self):
#         print("default")
# s1=student()#default

# class student :
#     def __init__(self):
#         self.name="deepika"
#         self.age=30
#         print("default",self.name,self.age)
# s1=student()#default deepika 30
# s2=student()#default deepika 30


# class student :
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print("parameter",self.name,self.age)
# s1=student("deep",30)# parameter deep 30
# s2=student("rash",20)#parameter rash 20


# class student :
#     def __init__(self):
#         print("address of self is",id(self))
# s1=student()
# print("id of s1 is ",id(s1))
# #address of self is 2205481005280
# #id of s1 is  2205481005280

# class counter:
#     def __init__(self):
#         self.count=0
#     def increment(self):
#         self.count+=1
#     def decrement(self):
#         self.count-=1
#     def getcount(self):
#         return self.count
# c1=counter()
# print(c1.getcount())#0
# c1.increment()
# c1.increment()
# print(c1.getcount())#2


# class student :
#     def __init__(self,name,address):
#         self.name=name
#         self.address=address
# s1=student("deep","chennai")
# s2=student("virat","banglore")

# class student :
#     def __init__(self,name,address):
#         self.name=name
#         self.address=address
#     def display(self):
#         print(self.name)
# s1=student("deep","chennai")
# s1.display()#deep
# print(s1.name)#deep
# s2=student("virat","banglore")
# s2.display()#virat
# print(s2.name)#virat

# class student :
#     def set(self,n,a):
#         self.name=n
#         self.address=a
#     def display(self):
#         print(self.name)
# s1=student()
# s1.set("deep","chenai")
# s1.display()#deep
# print(s1.name)#deep
# s2=student()
# s2.set("virat","ban")
# s2.display()#virat
# print(s2.name)#virat

# class student:
#     pass
# s1=student()
# s1.name="deep"
# print(s1.name)#deep


# class student:
#     def __init__(self):
#         self.name="virat"
# s1=student()
# s1.name="deep"
# print(s1.name)#deep


# class student:
#     def __init__(self):
#         self.name="virat"
#         print(self.name)#virat

# s1=student()
# s1.address="chenai"
# # print(s1.name)#deep
# print(s1.address)#chenai

# class student:
#     def __init__(self):
#         self.name="virat"
#         self.display()
#     def display(self):
#         print(self.name)

# s1=student()#virat


# class student :
#     college ="iit"
#     def __init__ (self,name):
#         self.name=name
# s1=student("deep")
# s2=student("rash")

# print(s1.name,"and",s1.college)#deep and iit
# print(s2.name,"and",s2.college)#rash and iit



# class student :
#     college ="iit"
#     def __init__ (self,name):
#         self.name=name
# s1=student("deep")
# s2=student("rash")

# print(s1.name,"and",s1.college)#deep and iit
# print(s2.name,"and",s2.college)#rash and iit
# student.college="NIT"
# print(s1.name,"and",s1.college)#deep and NIT
# print(s2.name,"and",s2.college)#rash and NIT


# class student :
#     college ="iit"
#     def __init__ (self,name):
#         self.name=name
# s1=student("deep")
# s2=student("rash")

# print(s1.name,"and",s1.college)#deep and iit
# print(s2.name,"and",s2.college)#rash and iit
# student.college="NIT"
# print(s1.name,"and",s1.college)#deep and NIT
# print(s2.name,"and",s2.college)#rash and NIT
# #1 using obecj
# print(s1.college)#nit

# #2.using class name
# print(student.college)#nit




# class student :
#     college ="iit"
#     def __init__ (self,name):
#         self.name=name
# s1=student("deep")
# s2=student("rash")

# print(s1.name,"and",s1.college)#deep and iit
# print(s2.name,"and",s2.college)#rash and iit
# s1.college="lncT"
# print(s1.name,"and",s1.college)#deep and lnct
# print(s2.name,"and",s2.college)#rash and NIT

