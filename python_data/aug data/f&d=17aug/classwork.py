# # fs=frozenset([1,2,3,4,5])
# # print(fs)

# # fs=frozenset((1,2,3,4,5))
# # print(fs)


# # fs=frozenset("python")
# # print(fs)

# # #fs=frozenset((1,2,3,4,5))
# # #fs.add(33)
# # #print(fs)#error

# # fs=frozenset([1,2,3,4,5])
# # a=frozenset([1,234324,52,431,1])
# # print(fs|a)

# # a=frozenset([1,2,3,4,5])
# # b=frozenset([1,234324,52,431,1])
# # a&=b
# # print(a)

# # #WAP to count unique elements in py using set.
# # text=input("enter the sentences")
# # words=text.split()
# # u=set(words)
# # print("count is ",len(u))

# # #WAP to check unique char in a string (means) wether all chr in a string unique or not .
# # text=input("enter the string")#.lower()
# # if len(text)==len(set(text)):
# #     print("char are unique")
# # else:
# #     print("not unique")
# #WAP to find first non repeating char in a string using set logic.
# text=input("enter the string").lower()
# t=set()
# t1=set()
# for i in text:
#     if text.count(i)> 1:
#         t1.add(i)
#     else:
#         t.add(i)
# for i in text:
#     if i not in t1:
#         print(i)
#         break



# text=input("enter string")
# seen=set()
# repeating=set()

# for char in text:
#    if char in seen:
#          repeating.add(char)
#    else:
#           seen.add(char)

# for char in text:
#      if char in seen and char not in repeating:
#            print("first non rep",char)
#            break
# else:
#     print("NO non rep characters")


#########dict##########
#d={key1:value1,key2:value2}
d={1:"java",2:"python",3:"react"}
print(d)

d=dict(a="abc",b="hello")
print(d)

student={
    "name":"abc",
    "age":39,
    "city":"indore"
}
print(student)
print(type(student))

student={
    "name":"abc",
    "age":39,
    "name":"bahubali"
}
print(student)
print(type(student))



student={
    "name":"abc",
    "age":39,
    "city":"abc"
}
print(student)