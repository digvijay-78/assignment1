# import pickle
# student={"id":101,
#          "name":"deep",
#          "course":"python"}
# f=open("student.dat","wb")
# pickle.dump(student,f)
# f.close()
# print("object serialized successfully")#��,

# import pickle
# student={"id":101,
#          "name":"deep",
#          "course":"python"}
# f=open("student.dat","rb")
# s=pickle.load(f)
# print(s,"object deserialized successfully")#{'id': 101, 'name': 'deep', 'course': 'python'} object deserialized successfully


# import pickle
# class Emp:
#     def __init__(self,id,name,salary):
#         self.id=id
#         self.name=name
#         self.salary=salary
#     def display(self):
#         print("id is",self.id)
#         print("name is",self.name)
#         print("salary is",self.salary)

# e1=Emp(101,"deep",909000)
# e2=Emp(102,"rash",12000)
# e3=Emp(103,"virat",15000)
# emp=[e1,e2,e3]
# f=open("employee121.dat","wb")
# pickle.dump(emp,f)
# f.close()
# print("done")

# f=open("employee121.dat","rb")
# l=pickle.load(f)

# for i in l:
#     i.display()
# f.close()
# """done
# id is 101
# name is deep
# salary is 909000
# id is 102
# name is rash
# salary is 12000
# id is 103
# name is virat
# salary is 15000"""

