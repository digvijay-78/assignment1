# class Emp:
#     def __init__(self,salary):
#         self.salary=salary
#     def getsalary(self):
#         return self.salary
# e=Emp(10000)
# print(e.getsalary())


# class Emp:
#     def __init__(self,salary):
#         self.__salary=salary
#     @property
#     def salary(self):
#         return self.__salary
# e=Emp(10000)
# print(e.salary)




# class Emp:
#     def __init__(self,name,salary):
#         self.__salary=salary
#         self.__name=name
#     @property
#     def salary(self):
#         return self.__salary
#     @property
#     def name(self):
#         return self.__name
#     @salary.setter
#     def salary(self,value):
#         self.__salary=value
#     @name.setter
#     def name(self,n):
#         self.__name=n

# e=Emp(10000,"yash")
# print(e.name)
# print(e.salary)

# # 10000
# # yash
# e.name="katappa"
# e.salary=1000000
# print(e.name)
# print(e.salary)
# # katappa
# # 1000000


# class Emp:
#     def __init__(self,name,salary):
#         self.__salary=salary
#         self.__name=name
#     @property
#     def salary(self):
#         return self.__salary
#     @property
#     def name(self):
#         return self.__name
#     @salary.setter
#     def salary(self,value):
#         self.__salary=value
#     @name.setter
#     def name(self,n):
#         self.__name=n
#     @salary.deleter
#     def salary(self):
#         print("deleting the salary")
#         del self.__salary
#     @name.deleter
#     def name(self):
#         print("deleting the name")
#         del self.__name

# e=Emp(10000,"yash")
# print(e.name)
# print(e.salary)

# # 10000
# # yash
# e.name="katappa"
# e.salary=1000000
# print(e.name)
# print(e.salary)
# # katappa
# # 1000000
# del e.salary
# del e.name
# print("done")
# # deleting the salary
# # deleting the name
# # done

# print(e.name)#AttributeError: 'Emp' object has no attribute '_Emp__name'


# class Student:
#     def __init__(self,rollno,name,salary):
#         self.__rollno=rollno
#         self.__name=name
#         self.__salary=salary
#     @property
#     def rollno(self):
#         return self.__rollno
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,n):
#         self.__name=n

#     @property
#     def salary(self):
#         return self.__salary
#     @salary.setter
#     def salary(self,value):
#         self.__salary=value

#     @salary.deleter
#     def salary(self):
#         print("deleting the salary")
#         del self.__salary
#     @name.deleter
#     def name(self):
#         print("deleting the name")
#         del self.__name
#     @rollno.deleter
#     def rollno(self):
#         raise AttributeError("name can not be deleted")
# s=Student("102","deep",128)
# print(s.rollno)
# print(s.name)
# print(s.salary)        

# s.name="katappa"
# s.salary=1000000
# print(s.name)
# print(s.salary)

# del s.salary
# del s.name
# print("done")


# class Parent:
#     def fun1(self):
#         print("parent function 1")
# class Child(Parent):
#     def fun2(self):
#         print("child function 2")

# obj=Child()
# obj.fun1()
# obj.fun2()
# """parent function 1
# child function 2"""




# class Person:
#     def fun1(self):
#         print("person function 1")
# class Employee(Person):
#     def fun2(self):
#         print("employee function 2")
# class Manager(Employee):
#     def fun3(self):
#         print("manager function 3")

# obj=Manager()
# obj.fun1()
# obj.fun2()
# obj.fun3()
# """person function 1
# employee function 2
# manager function 3"""


# class Person:
#     def __init__(self):
#         print("person class constructor ")
# class Employee(Person):
#     def __init__(self):
#         print("employee function 2")
# obj=Employee()#employee function 2


class Person:
    def __init__(self,name,address,age):
        print("person class constructor ")
        self.name=name
        self.address=address
        self.age=age
class Employee(Person):
    def __init__(self,name,address,age,salary):
        print("employee function 2")
        super().__init__(name,address,age)
        self.salary=salary
    def display(self):
        print(self.name,"and",self.address,"",self.age,"and",self.salary)


obj=Employee("deep","chennai",30,89999)
obj.display()
"""employee function 2
person class constructor 
deep and chennai  30 and 89999"""