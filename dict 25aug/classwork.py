'''student={
    101:{"name":"deep","age":30},
    102:{"name":"rash","age":32}
}
# for id,details in student.items():
#     print(id)
#     for k,v in details.items():
#         print(k,v)

# del student[101]["age"]
# print(student[101])#{'name': 'deep'}

student={
    101:{"name":"deep","age":30},
    102:{"name":"rash","age":32}
}
del student[101]
print(student)#{102: {'name': 'rash', 'age': 32}}

# d={}
# key=[1,2,3]
# d[key]="deep"
# print(d)#TypeError: unhashable type: 'list'


d={}
key=(1,2,3)
d[key]="deep"
print(d)#{(1, 2, 3): 'deep'}


# d={}
# key=(1,2,3,[7948,65])
# d[key]="deep"
# print(d)#TypeError: unhashable type: 'list'

a=eval(input("enter the val"))
print(a)

print(type(a))
# <class 'int'>

# enter the val10.5
# 10.5
# <class 'float'>
# enter the val"abc"
# abc
# <class 'str'>


#WAP to take dict. from keyboard and print sum of value 
n=int(input("enter the no of item "))
d={}
for i in range(n):
    key=input("enter key :")
    value=int(input("enter value"))
    d[key]=value

s=sum(d.values())
print("sum is",s)#enter the no of item 2
# enter key :a
# enter value154
# enter key :s
# enter value365458
# sum is 365612

d=eval(input("enter the dict"))
s=sum(d.values())
print(d)
print("sum is",s)
# enter the dict{"a":11,"b":22,"c":33}
# {'a': 11, 'b': 22, 'c': 33}
# sum is 66

#WAP TO FIND NO. OF OCCURANCE OF EACH LETTER PRESENT IN THE GIVEN STRING
word=input("enter string")
d={}
for i in word:
    d[i]=d.get(i,0)+1
print(d)

for k,v in d.items():
    print(k,"occured",v,"times")
# enter stringhello
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}
# h occured 1 times
# e occured 1 times
# l occured 2 times
# o occured 1 times

#WAP TO SORT AND FIND OCURANCE
word=input("enter string")
d={}
for i in word:
    d[i]=d.get(i,0)+1
print(d)

for k,v in sorted( d.items()):
    print(k,"occured",v,"times")

# enter stringHELLO
# {'H': 1, 'E': 1, 'L': 2, 'O': 1}
# E occured 1 times
# H occured 1 times
# L occured 2 times
# O occured 1 times

#WAP TO FIND NO. OF OCCURANCE OF EACH VOVEL PRESEND IN THE GIVEN STRING 
word=input("enter string")
d={}
for i in word:
 if i in "aeiou":
    d[i]=d.get(i,0)+1
print(d)

for k,v in sorted( d.items()):
    print(k,"occured",v,"times")
# enter stringhello
# {'e': 1, 'o': 1}
# e occured 1 times
# o occured 1 times

'''

#WAP TO TRACK HOW MANY TIMES EACH USER TRIED TO LOGIN 
logins=["deep","rash","kattapa","deep","rash","kattapa"]
d={}
for user in logins:
   d[user]=d.get(user,0)+1

print(d)#{'deep': 2, 'rash': 2, 'kattapa': 2}


#WAP TO GROUP WORDS BASED ON THEIR LENGTH 
words=["cat","dog","lion","tiger","ant"]
d={}
for word in words:
   l=len(word)
   if l not in d:
        d[l]=[]
   d[l].append(word)

print(d)#{3: ['cat', 'dog', 'ant'], 4: ['lion'], 5: ['tiger']}


#WAP TO MERGE TO 2 DICT AND SUM VALUES 

store1={"apple":10,"banana":20,"orange":8}
store2={"apple":10,"banana":20,"graps":40}
print(store1)
print(store2)
merged=store1.copy()
for k,v in store2.items():
    merged[k]=merged.get(k,0)+v
print(merged)
# {'apple': 10, 'banana': 20, 'orange': 8}
# {'apple': 10, 'banana': 20, 'graps': 40}
# {'apple': 20, 'banana': 40, 'orange': 8, 'graps': 40}

