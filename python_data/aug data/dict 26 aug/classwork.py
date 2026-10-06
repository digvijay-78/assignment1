# def function_name(parameters):
#     body of function 
#     return Value
'''
def hello():
    print("hello guys")
def bye():
    print("bye guys")
hello()
hello()
bye()
# hello guys
# hello guys
# bye guys

#hello()
#def hello():
#    print("hello guys")#NameError: name 'hello' is not defined. Did you mean: 'help'?

def sum():
    a=10
    b=20
    c=a+b
    print("sum is",c)
sum()#sum is 30


def sum(a,b):
    c=a+b
    print("sum is",c)
sum(100,200)#sum is 300
#sum()#TypeError: sum() missing 2 required positional arguments: 'a' and 'b'


def hello(name):
    print("heyyyyy",name)
hello("abc")
hello(20)
#heyyyyy abc
#heyyyyy 20
'''


# def hello(name):
#     print("heyyyyy",name)
# def sum (a,b):
#     print(a+b)
# print("start")
# name=input("enter name ")
# hello(name)
# x=int(input("first no"))
# y=int(input("second no"))
# sum(x,y)
# print("done")

# start
# enter name yash
# heyyyyy yash
# first no724
# second no76
# 800
# done


# def hello(name):
#     print("heyyyyy",name)
# def sum (a,b):
#     print(a+b)
#     hello("deep")
#     hello("rash")

# print("start")
# name=input("enter name ")
# hello(name)
# x=int(input("first no"))
# y=int(input("second no"))
# sum(x,y)
# print("done")

# start
# enter name yash
# heyyyyy yash
# first no10
# second no20
# 30
# heyyyyy deep
# heyyyyy rash
# done


# def sum (a,b):
#     c=a+b
#     print("sum is ",c)
#     print("sum end")
# print("start")
# sum(10,20)
# #print("sum is ",c)#NameError: name 'c' is not defined
# print("done")


# def sum (a,b):
#     c=a+b
#     print("sum end")
#     return c
# print("start")
# x=sum(10,20)
# print("sum is ",x)
# print("done")
# # start
# # sum end
# # sum is  30
# # done



# # def sum (a,b):
# #     c=a+b
# #     print("sum end")
# #     return c
# # print("start")
# # print("sum is ",sum(10,20))
# # print("Done")
# # start
# # sum end
# # sum is  30
# # Done


# def sum (a,b):
#     c=a+b
#     print("sum end")

# print("start")
# print("sum is ",sum(10,20))
# print("Done")

# start
# sum end
# sum is  None
# Done

# def test():
#     print("test started")
#     return
#     print("test ended ")
# print("start")
# test()
# print("done")

# # start
# # test started
# # done

# def calculate(a,b):
#     print("fun started")
#     x=a+b
#     y=a-b
#     return x,y
# print("start")
# result=calculate(20,10)
# print(result)
# print("done")
# start
# fun started
# (30, 10)
# done


# def calculate(a,b):
#     print("fun started")
#     x=a+b
#     y=a-b
#     return x,y
# print("start")
# sum,diff=calculate(20,10)
# print("sum is ",sum)
# print("diff is ",diff)
# print("done")

# start
# fun started
# sum is  30
# diff is  10
# done

#WAP to create a function which recive 1 paramter as a no. and 
# return list of all the even no. up to that no.
def evenlist(n):
    even=[]
    a=int(input("enter the no"))
    for i in range(1,a):
        if i%2==0:
            even.append(i)
    return even
print("start")
result=evenlist(10)
print("result is",result)

# start
# enter the no20
# result is [2, 4, 6, 8, 10, 12, 14, 16, 18]