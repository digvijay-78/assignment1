# filter(fun,iterable)
# num=[1,2,3,4,5,6,7,8]
# def even(x):
#     if x%2==0:
#         return x
# res=list(filter(even,num))
# print(res)#[2, 4, 6, 8]


# num=[1,2,3,4,5,6,7,8]
# res=list(filter(lambda x:x%2==0,num))
# print(res)#[2, 4, 6, 8]

# n=["abc","abhi","avi","rash","deep"]
# res=list(filter(lambda x:x.startswith("a"),n))
# print(res)#['abc', 'abhi', 'avi']

#WAP to filter names of stuents whose lenth is greater than 5 
# n=["abc","abhi","avi","rashmika","deep"]
# res=list(filter(lambda x:len(x)>5,n))
# print(res)#['rashmika']

# #WAP to filter all the palendorne words
# n=["madam","level","java","python"]
# res=list(filter(lambda x:x==x[::-1],n))
# print(res)#['madam', 'level']

# from functools import reduce
# reduce(function,iterable,initializer)
# from functools import reduce
# def add(x,y):
#     return x+y
# num=[1,2,3,4,5]
# res=reduce(add,num)
# print(res)#15

# from functools import reduce
# def add(x,y):
#     return x+y
# num=[1,2,3,4,5]
# res=reduce(add,num,100)
# print(res)#115


# from functools import reduce
# num=[1,2,3,4,5]
# res=reduce(lambda x,y :x+y,num,100)
# print(res)#115

# from functools import reduce
# num=[1,2,3,4,5]
# res=reduce(lambda x,y :x+y,num)
# print(res)#15

# #WAP to multiply all the elemnts of list using reduce


# from functools import reduce
# num=[1,2,3,4,5]
# res=reduce(lambda x,y :x*y,num)
# print(res)#120

# from functools import reduce
# def mul(x,y):
#     return x*y
# num=[1,2,3,4,5]
# res=reduce(mul,num,100)
# print(res)#12000



#WAP to find maximum element in list using reduce
# from functools import reduce
# num=[1,2,3,4,5]
# res=reduce(lambda x,y:x if x>y else y ,num)
# print(res)#5


# #WAP to concatnate string in a list using using reduce
# from functools import reduce
# word=["jave","is","missing"]
# res=reduce(lambda x,y :x+" "+y,word)
# print(res)#jave is missing

# num=[14,32,36,6536,36,3632,35131,546]
# res=sorted(num)
# print(res)#[14, 32, 36, 36, 546, 3632, 6536, 35131]



# #SYNTAX
# sorted(iterable,key=None,reverse=False)

# num=[14,32,36,6536,36,3632,35131,546]
# res=sorted(num,reverse=True)
# print(res)#[35131, 6536, 3632, 546, 36, 36, 32, 14]


# w=["java","python","c"]
# res=sorted(w,key=lambda x:len(x))
# print(res)#['c', 'java', 'python']


# n=[("abc",20),("xyz",18),("www",30),("bbb",40)]
# res=sorted(n)
# print(res)#[('abc', 20), ('bbb', 40), ('www', 30), ('xyz', 18)]


# n=[("abc",20),("xyz",18),("www",30),("bbb",40)]
# res=sorted(n,key=lambda x:x[-1])
# print(res)#[('xyz', 18), ('abc', 20), ('www', 30), ('bbb', 40)]


# n=[("abc",20),("xyz",18),("www",30),("bbb",40)]
# res=sorted(n,key=lambda x:x[-1],reverse=True)
# print(res)#[('bbb', 40), ('www', 30), ('abc', 20), ('xyz', 18)]


# marks={"abc":80,"xzy":90,"www":44,"bbb":70}
# res=sorted(marks)
# print(res)#['abc', 'bbb', 'www', 'xzy']


# marks={"abc":80,"xzy":90,"www":44,"bbb":70}
# res=sorted(marks.items())
# print(res)#[('abc', 80), ('bbb', 70), ('www', 44), ('xzy', 90)]



# marks={"abc":80,"xzy":90,"www":44,"bbb":70}
# res=sorted(marks.items(),key=lambda x:x[-1])
# print(res)#[('www', 44), ('bbb', 70), ('abc', 80), ('xzy', 90)]

# n=["abc","Abc","bbc","BBC"]
# res=sorted(n,key=lambda x:x.lower())
# print(res)#['abc', 'Abc', 'bbc', 'BBC']

# pro=[
#     {"name":"laptop","price":8000},
#     {"name":"mobile","price":4000},
#     {"name":"tablet","price":3000}
# ]
# res=sorted(pro,key=lambda x:x["price"])
# print(res)#[{'name': 'tablet', 'price': 3000}, {'name': 'mobile', 'price': 4000}, {'name': 'laptop', 'price': 8000}]


# lambda x:
#     y=x+2
#     return y
# invalid

# lambda x:y=x+2

# invalid


# lambda x:
#     for i in range(x):
#         print(i)
# invalid

# lambda x:print(x)
# invalid