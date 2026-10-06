# file=open("batch19.txt")
# print(file)#<_io.TextIOWrapper name='batch19.txt' mode='r' encoding='cp65001'>

# f=open("batch19.txt")
# print(f)
# print("file name",f.name)
# print("mode",f.mode)
# print("open/close",f.closed)
# """<_io.TextIOWrapper name='batch19.txt' mode='r' encoding='cp65001'>
# file name batch19.txt
# mode r
# open/close False"""


# f=open("batch19.txt")
# d=f.read()
# print(d)#hello guys


# with open("batch19.txt","r") as f:
#     data=f.read()
#     print(data)

# with open("batch19.txt","w") as f:
#     data=f.write("what a life")
#     print("done")#file data change from hello guys to "what a life"


# with open("batch119.txt","w") as f:
#     data=f.write("what a life")
#     print("done")#new file banadi


# with open("batch19.txt","a") as f:
#     data=f.write("end of python")
#     print("done")#what a lifeend of python



# with open("batch19.txt","x") as f:
#     data=f.write("end of python")
#     print("done")#FileExistsError: [Errno 17] File exists: 'batch19.txt'
# with open("batch109.txt","x") as f:
#     data=f.write("end of python")
#     print("done")#end of python

# with open("batch109.txt","r+") as f:
#     data=f.read()
#     print(data)
#     f.write("new data added using r+")
#     print("done")

# """2 baar chalana padega 
# hey guys
# done
# hey guysnew data added using r+
# done"""



# with open("batch49.txt","w+") as f:
#     f.write("hello world")
#     print(f.read())
#     print("done")

# """empty rahega
# done"""


# with open("batch49.txt","w+") as f:
#     f.write("hello world")
#     f.seek(0)
#     print(f.read())
#     print("done")

# """ hello world
# done"""


# with open("batch49.txt","a+") as f:
#     f.write(" Python  world")
#     f.seek(0)
#     print(f.read())
#     print("done")

# """hello world Python  world
# done"""


# f1=open("abc.webp","rb")
# d=f1.read()
# f2=open("next.webp","wb")
# f2.write(d)



# f1=open("batch19.txt","rb")
# print(f1.tell())
# print(f1.read(3))
# print(f1.tell())
# """0
# b'wha'
# 3"""


# f1=open("batch19.txt","rb")
# f1.seek(5)
# print(f1.read())
# print(f1.tell())
# """b'a lifeend of python'
# 24"""


# import json
# emp=[{"id":1,"name":"deep"},{"id":2,"name":"rash"}]
# with open ("emp.json","w") as f:
#     json.dump(emp,f)#file bangai 

# import json
# with open ("emp.json","r") as f:
#     d=json.load(f)
#     print(d)#[{'id': 1, 'name': 'deep'}, {'id': 2, 'name': 'rash'}]

# f=open("batch19.txt","r")
# print(f.readline())
# print(f.readline())
# """hello world

# java
# """


f=open("batch19.txt","r")
# while True:
#     l=(f.readline())
#     if not l:
#         break
#     print(l)
# """hello world

# java

# python 

# react

# DSA"""

# f=open("batch19.txt","r")
# l=(f.readlines())
# print(l)
# print(l[0])
# print(l[1])
# """['hello world\n', 'java\n', 'python \n', 'react\n', 'DSA']
# hello world

# java
# """


# #WAP to read a file and display total no of lines and total no of words

# lines_count=0
# words_counts=0
# with open("batch19.txt","r") as f:
#     for line in f:
#         lines_count+=1
#         words_counts+=len(line.split())
# print(lines_count)#5
# print(words_counts)#6


# f=open("batch19.txt","r")
# l=(f.readlines())
# c=0
# print("Line:",len(l))
# for i in l:
#     m=i.split()
#     c+=len(m)

# print(c)
# """Line: 5
# 6"""

# #WAP to read a file and display total no of lines and total no of words without space line

# lines_count=0
# words_counts=0
# with open("batch19.txt","r") as f:
#     for line in f:
#         if line.strip():
#             lines_count+=1
#             words_counts+=len(line.split())
# print(lines_count)#5
# print(words_counts)#6

#WE HAVE A TEXTFILE WITH NAME AND MARKS WAP TO FIND HIGHEST MARKS , AVG MARKS AND PRINT TOPPER NAME

try :
    with open("batch19.txt","r") as f:
        t=0
        c=0
        hmarks=-1
        topper=""
        for line in f:
            parts=line.strip().split()
            name=parts[0]
            marks=int(parts[1])
            t+=marks
            c+=1
            if marks>hmarks:
                hmarks=marks
                topper=name
        avg=t/c
        print("topper name :",topper)
        print("topper marks :",hmarks)
        print("avg marks :",avg)
except FileNotFoundError:
    print("invalid")

"""topper name : katappa
topper marks : 90
avg marks : 81.66666666666667"""
 