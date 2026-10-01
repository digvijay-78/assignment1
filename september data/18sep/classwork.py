# class hello:
#     x=10
# print(type(hello))#<class 'type'>
# print((hello.__dict__))
# hello.y=20
# print(hello.__dict__)# 'y': 20}
# del hello.y
# print(hello.y)#AttributeError: type object 'hello' has no attribute 'y'



# class student :
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def displayname(self):
#         print(f"Name is {self.name}")
#     def display_marks(self):
#         print(f"marks is :{self.marks}")
#     def display_all(self):
#         self.displayname()
#         self.display_marks()

# s1=student("deeika",90)
# s1.display_all()
#Name is deeika
#marks is :90


# class student :
#     def __init__(self,name):
#         self.name=name
#         self.marks=0
#     def setmarks(self,marks):
#         self.marks=marks
#         return self
#     def hello(self):
#         print(f"hello this  is {self.name}")
#         return self
#     def display(self):
#         print(f"marks is :{self.marks}")
#         return self
#     def bye (self):
#         print("all done")
# s1=student("deeika")
# s1.hello().setmarks(88).display().bye()
# #hello this  is deeika
# #marks is :88
# #all done


# class stuf:
#     def __init__(self):
#         self._marks=90
#         print(self._marks)#90
# o=stuf()
# print(o._marks)#90


# class stuf:
#     def __init__(self):
#         self.__salary=900000
#     def display(self):
#         print(self.__salary)#90000
# o=stuf()
# o.display()
# print(o.__salary)#AttributeError: 'stuf' object has no attribute '__salary'


# class stuf:
#     def __init__(self):
#         self.__salary=900000
#     def display(self):
#         print(self.__salary)#90000
# o=stuf()
# o.display()
# print(o._stuf__salary)#90000

# class stuf:
#     def __init__(self):
#         self.__salary=0
#         self.name=""
#     def set_salary(self,salary):
#         self.__salary=salary
#     def get_salary(self):
#         return self.__salary
#     def set_name(self,name):
#         self.__name=name
#     def get_name(self):
#         return self.__name

# o=stuf()
# print(o.get_salary())#0
# o.set_salary(9999)
# print(o.get_salary())#9999
# o.set_name("rash")
# print(o.get_name())#rash


class Emp:
    def __init__(self,id,name,salary):
        self.__id=id
        self.__name=name
        self.__salary=salary
    def get_id (self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_salary(self):
        return self.__salary

    def set_id(self,id):
        self.__id=id
    def set_name(self,name):
        if name.strip()!="":
            self.__name=name
        else:
            print("name can't be empty")
            self.__name="unkown"
    def set_salary(self,salary):
        if salary>0:
            self.__salary=salary
        else:
            print("invalid salary")
            self.__salary=0
    def display(self):
        print("ID is ",self.__id)
        print("Name is ",self.__name)
        print("salary is ",self.__salary)

eid=int(input("enter the id"))
ename=input("enter the name")
esalary=int(input("enter the salary"))

obj1=Emp(eid,ename,esalary)
obj1.display()

print(obj1.get_id())
print(obj1.get_name())
print(obj1.get_salary())

obj1.set_name("")
print(obj1.get_name())
"""enter the id121
enter the nameyash
enter the salary2000
ID is  121
Name is  yash
salary is  2000
121
yash
2000
name can't be empty
unkown"""