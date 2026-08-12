'''
t=(10,20,30)
print(20 in t)
print(20  not in t)

t=(10,20,30)
t2=(1,2,4)
print(t < t2)


t=(10,20,30)
#del t[0]
del t
print(t)


t=(10,20,30)
L=list(t)
print(L)



t=(10,20,30)
print(sorted(t))

import sys
a=("learn","py","hello")
print(sys.getsizeof(a))

b=["learn","py","hello"]
print(sys.getsizeof(b))



from collections import namedtuple
student=namedtuple("student",["name","age","city"])

s1=student("deepika",30,"chennai")
print(s1.name)
print(s1.age)
print(s1.city)



#WAP to store acc. details in named tuple 
from collections import namedtuple
account=namedtuple("account",["accno","holdername","balance"])

accno=int(input("enter the acc no"))
name=input("enter the acc holder name")
balance=float(input("enter the balance"))

acc=account(accno,name,balance)
print("details")
print(acc.accno)
print(acc.holdername)
print(acc.balance)
'''

from collections import namedtuple
student=namedtuple("student",["rollno","name","marks"])
n=int(input("enter no of students"))
students=[]
for i in range(n):
    print("enter details")
    r=int(input("enter rollno"))
    name=input("enter name")
    m=float(input("enter marks"))
    s=student(r,name,m)
    students.append(s)
print("Details")
for x in students:
    print("roll no.",x.rollno,x.name,"and marks are ",x.marks)

