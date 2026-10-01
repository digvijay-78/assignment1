# print("start ")#start
# a=10
# b=0

# print(a/b)#ZeroDivisionError: division by zero
# print("done")#nahi chalega


# print("start ")#start
# try:
#     a=int(input())
#     b=int(input())
#     print(a/b)
# except:
#     print("error came")
# print("done")
# """start 
# 10
# 0
# error came
# done"""

# print("start")
# a=int(input("enter the value"))
# print(a)

# try:
#     #where problem may occur
# except Exceptiontype 1:
#     #handle exception 2
# except Exceptiontype 2:
#     #handle exception 2
# except Exceptiontype 3:
#     #handle exception3
# else:
#     #runs if no exception occur
# finally:
#     #always execute

# print("start")
# try:
#     print("try start ")
#     x=int("abc")
#     print("try end")
# except:
#     print("something went worong")
#     print("except end")
# print("program end")
# """start
# try start 
# something went worong
# except end
# program end"""

# print("start")
# try:
#     print("try start ")
#     x=int("abc")
#     print("try end")
# except ValueError:
#     print("please enter integer value")
#     print("except end")
# print("program end")
# """tart
# try start 
# please enter integer value
# except end
# program end"""

# print("start")
# try:
#     print("try start ")
#     x=int(input("enter the x"))
#     a=int(input("enter a"))
#     b=int(input("enter b"))
#     print(a/b)
#     print("try end")
# except ValueError:
#     print("please enter integer value")
#     print("except end")
# except ZeroDivisionError:
#     print("do not give zero ")
# print("program end")
# """start
# try start
# enter the x10
# enter a20
# enter b0
# do not give zero
# program end"""

# print("st")
# try:
#     print("hello"+5)
# except TypeError:
#     print("please check operation")
# print("end")
# """st
# please check operation
# end"""

#print("st")
# try:
#     t=[10,20,30]
#     print(t[5])
# except TypeError:
#     print("please check operation")
# except IndexError:
#     print("check index")
# print("end")
# """st
# check index
# end"""

print("st")
try:
    t={"a":1}
    print(t["b"])
except TypeError:
    print("please check operation")
except IndexError:
    print("check index")
except KeyError:
    print("check key")
print("end")
"""st
check key
end"""