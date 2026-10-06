# print("start")
# try:
#     x=10
#     x.append(5)
# except AttributeError:
#     print("attribute not found")
# print("program end")
# """start
# attribute not found
# program end"""

# print("start")
# try:
#     import XYZ
# except ModuleNotFoundError:
#     print("check the module")
# print("program end")
# """start
# check the module
# program end"""



# print("start")
# try:
#     f=open("alpha.txt")
# except FileNotFoundError:
#     print("create file first")
# print("program end")
# """start
# create file first
# program end"""

# print("start")
# import math
# try:
#     print(math.exp(10))
#     import XYZ
# except BaseException:
#     print("result")
# except Exception:
#     print("chalne doi")
# except OverflowError:
#     print("result is to large")
# print("program end")
# """start
# 22026.465794806718
# result
# program end"""

# print("start")
# import math
# try:
#     x=int("abc")
#     math.exp(10000)
# except (OverflowError , ValueError):
#     print("overflow or value problems")
# except BaseException:
#     print("genral parent class")
# print("program end")
# """start
# overflow or value problems
# program end"""


# print("start")
# import math
# try:
#     x=int(input("enter the value"))
#     print("user enter correct value")
#     a=int(input("enter the value"))
#     b=int(input("enter the value"))
#     print(a/b)
#     print("divison work done")
# except (ZeroDivisionError , ValueError) as e:
#     print("problem occured ",e)
# print("program end")
# """start
# enter the valuefdf
# problem occured  invalid literal for int() with base 10: 'fdf'
# program end
# start
# enter the value10
# user enter correct value
# enter the value20
# enter the value0
# problem occured  division by zero
# program end
# """


# print("start")
# import math
# try:
#     x=int(input("enter the value"))
#     print("user enter correct value")
#     a=int(input("enter the value"))
#     b=int(input("enter the value"))
#     z=(a/b)
# except ( ValueError) as e:
#     print("problem occured ",e)
# else:
#     print("value of x is ",x)
#     print("value of z is ",z)
# print("program end")
# """
# start
# enter the value10
# user enter correct value
# enter the value20
# enter the value9
# value of x is  10
# value of z is  2.2222222222222223
# program end

# start
# enter the valueqd
# problem occured  invalid literal for int() with base 10: 'qd'
# program end
# """


# print("start")
# import math
# try:
#     x=int(input("enter the value"))
#     print("user enter correct value")
#     a=int(input("enter the value"))
#     b=int(input("enter the value"))
#     z=(a/b)
# except ( ValueError) as e:
#     print("problem occured ",e)
# finally:
#     print("this is finally block")
# print("program end")
# """
# start
# enter the valuep
# problem occured  invalid literal for int() with base 10: 'p'
# this is finally block
# program end

# start
# enter the value10
# user enter correct value
# enter the value20
# enter the value0
# this is finally block
# Traceback (most recent call last):
#   File "d:\infobeans\1oct\classwork.py", line 130, in <module>
#     z=(a/b)
#        ~^~
# ZeroDivisionError: division by zero
# """

# print("start")
# import math
# try:
#     x=int(input("enter the value"))
#     print("user enter correct value")
#     a=int(input("enter the value"))
#     b=int(input("enter the value"))
#     z=(a/b)
# finally:
#     print("this is finally block")
# print("program end")
# """
# start
# enter the value10
# user enter correct value
# enter the value20
# enter the value2
# this is finally block
# program end

# start
# enter the value1
# user enter correct value
# enter the value20
# enter the value0
# this is finally block
# Traceback (most recent call last):
#   File "d:\infobeans\1oct\classwork.py", line 163, in <module>
#     z=(a/b)
#        ~^~
# ZeroDivisionError: division by zero
# """



# print("start")
# import math
# try:
#     x=int(input("enter the value"))
#     print("user enter correct value")
#     a=int(input("enter the value"))
#     b=int(input("enter the value"))
#     z=(a/b)

# print("program end")
# """
# SyntaxError: expected 'except' or 'finally' block
# """


# print("start")
# import math
# file=None
# try:
#     file=open("text1.txt","r")
#     data=file.read()
#     print(data)
# except FileNotFoundError as e:
#     print("problem occured",e)
# finally:
#     print("closing the file")
#     if file :
#         file.close()
# print("program end")
# """
# start
# problem occured [Errno 2] No such file or directory: 'text1.txt'
# closing the file
# program end
# """

# def test():
#     try :
#         return "from try"
#     finally:
#         return "from finally"
# print(test())
# print("program end")
# """from finally
# program end"""

# def test():
#     try :
#         return "from try"
#     finally:
#         print( "from finally")
# print(test())
# print("program end")
# """from finally
# from try
# program end"""


# def test():
#     try :
#         print("from try")
#     finally:
#         print( "from finally")
# print(test())
# print("program end")
# """from try
# from finally
# None
# program end"""

# def test():
#     try :
#         return 10/0
#     except ZeroDivisionError:
#         return "error handled"
#     finally:
#         print( "from finally")
# print(test())
# print("program end")
# """
# from finally
# error handled
# program end
# """


# import os
# try :
#     print("try bloack")
#     os._exit(0)
# finally:
#     print( "from finally")
# """
# try bloack
# """


# class ageerror(Exception):
#     pass
# age=int(input("enter age"))
# if age <18:
#     raise ageerror("you are not eligible")
# print("you are allowed")#ageerror: you are not eligible

# def Withdraw(amount):
#     balance=5000
#     if amount >balance:
#         raise Exception("insufficent balance")
#     return balance-amount
# try:

#     print(Withdraw(2000))
# except Exception as e:
#     print("error is ",e)
# print("more requierd code")
# """error is  insufficent balance
# more requierd code
# 3000
# more requierd code
# """

# class Balance(Exception):
#     pass
# def Withdraw(amount):
#     balance=5000
#     if amount >balance:
#         raise Balance("insufficent balance")
#     return balance-amount
# try:

#     print(Withdraw(6000))
# except Balance as e:
#     print("error is ",e)
# print("more requierd code")
# """error is  insufficent balance
# more requierd code
# """



class DotException(Exception):
    pass
class AtTheRateException(Exception):
    pass
class DomainException(Exception):
    pass

def validateemail(email):
    if email.count("@")!=1:
        raise AtTheRateException ("Invalid @ usage")
    elif email.count(".")!=1:
        raise DotException("Invalid '.' usage")
    elif "com" not in email or "in" not in email or "net" not in email :
        raise DomainException("invalid domain")

email=input("enter the email")
try :
    validateemail(email)
    print("valid email")
except DotException as e:
    print("error",e)
    print("invalid email")
except AtTheRateException as e:
    print("error",e)
    print("invalid email")
except DomainException as e:
    print("error ",e)
    print("invalid email")
else:
    print("vailid hai")
