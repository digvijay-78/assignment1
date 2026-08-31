# students={"name":"deep","marks":[80,90]}
# print(students)
# new=students.copy()
# new["marks"][0]=50
# print(students)
# print(new)

# print(id(students))
# print(id(new))

# import copy
# students={"name":"deep","marks":[80,90]}
# print(students)
# new=copy.deepcopy(students)
# print(new)
# new.update({"new":"aree"})
# new["marks"][0]=50
# print(students)
# print(new)


# dict comprehesion :-
#======================
#{keyexpression:value expression for item in iterable}

# square={}
# for i in range(1,6):
#     square[i]=i*i
# print(square)#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# square={i:i*i for i in range(1,6)}
# print(square)#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# square={i:i*i for i in range(1,6) if i%2==0}
# print(square)#{2: 4, 4: 16}


# words=["apple","banana","mango"]
# d={word:len(word) for word in words}
# print(d)#{'apple': 5, 'banana': 6, 'mango': 5}

# d={"a":1,"b":2,"c":3}
# print(d)
# another={value:key for key,value in d.items()}
# print(another)

# l=[1,2,3,4,5,6]
# print(l)#[1, 2, 3, 4, 5, 6]
# another={x:"even" if x%2==0 else "odd" for x in l}
# print(another)#{1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd', 6: 'even'}

# key=["name","age","city"]
# values=["deep",30,"chennai"]
# d={key[i]:values[i] for i in range(len(key))}
# print(d)#{'name': 'deep', 'age': 30, 'city': 'chennai'}

# #WAP to count frequency of a char.
# t="programming" 
# d={c:t.count(c) for c in t}
# print(d)#{'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}

# #nested 
# {
# key1:{
#     innerkey:val1
#     inner2:val 2

# },
# key2:{
#     inner3:val3
#     inner4:val4
# }
# }
# student={
#     101:{"name":"katappa","age":30},
#     102:{"name":"katappa","age":20},
#     103:{"name":"katappa","age":30}
# }
# print(student)
# print(student[101])
# print(student[101]["name"])

# student={
#     101:{"name":"katappa","age":30},
#     102:{"name":"katappa","age":20},
#     103:{"name":"katappa","age":30}
# }
# student[101]["age"]=90
# print(student[101])#{'name': 'katappa', 'age': 90}


# student={
#     101:{"name":"katappa","age":30},
#     102:{"name":"katappa","age":20},
#     103:{"name":"katappa","age":30}
# }
# student[101]["city"]="chennai"
# print(student[101])#{'name': 'katappa', 'age': 30, 'city': 'chennai'}




# student={
#     101:{"name":"katappa","age":30},
#     102:{"name":"katappa","age":20},
#     103:{"name":"katappa","age":30}
# }
# student[104]={"name":"deep","age":32}
# print(student[104])#{'name': 'deep', 'age': 32}



# student={
#     101:{"name":"katappa","age":30},
#     102:{"name":"katappa","age":20},
#     103:{"name":"katappa","age":30}
# }
# for id,details in student.items():
#     print(id,"and",details)

# # 101 and {'name': 'katappa', 'age': 30}
# # 102 and {'name': 'katappa', 'age': 20}
# # 103 and {'name': 'katappa', 'age': 30}





# student={
#     101:{"name":"katappa","age":30},
#     102:{"name":"katappa","age":20},
#     103:{"name":"katappa","age":30}
# }
# for id,details in student.items():
#     print("id",id)
#     for k,v in details.items():
#         print(k,"and ",v)