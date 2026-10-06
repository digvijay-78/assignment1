from collections import namedtuple
student=namedtuple("student",["roll","name", "marks"])
s=student(101,"abs",23)
print(student._fields)

from collections import namedtuple
student=namedtuple("student",["roll","name", "marks"])
s=student(101,"abs",23)
print(s._asdict())


from collections import namedtuple
student=namedtuple("student",["roll","name", "marks"])
s=student(101,"abs",23)
s2=s._replace(marks=75)
print("after replacing ",s2)


from collections import namedtuple
student=namedtuple("student",["name","age", "marks"])
data=("deep",30,"indore")
s=student._make(data)
print(s)
print(s.name)
print(s.age)





#sets
s=set((1,3,2,42,3,3,43,241,4,1,4,2))
print(s)
print(type(s))

s={}
print(s)
print(type(s))#dict

s={"bda","deepika","rashmika","deepika"}
print(s)



s={"bda","deepika","rashmika","deepika",10,True,True}
print("deepika" in s)
print(20 in s)

s={10,20,30}
s.add(2)
print(s)

s={10,20,30}
s.update((23,4,5))
print(s)

s={10,20,30}
s.discard(20)
s.discard(2)
print(s)



d={1,2,3,4,5,6}
for i in range(1,4):
    d.discard(i)

print(d)


d={1,534,234,4,5,6}
for i in range(1,4):
    d.discard(i)

print(d)



s={"bda","deepika","rashmika","via"}
x=s.pop()
print("removed",x)

s={"bda","deepika","rashmika","via"}
s.clear()
print(s)


s=set()
s.clear()
print(s)