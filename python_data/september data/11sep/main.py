# import mymath
# print(mymath.add(10,20))#30
# print(mymath.sub(10,20))#-10
# print(mymath.mul(10,20))#200

# from mymath import add
# print(add(10,20))#30

# from mymath import *
# print(add(10,20))#30
# print(mul(20,2))#40

# import mymath as m
# print(m.mul(2,20))#40


# import myvariable as v
# print(v.PI)
# print(v.company)
# #3.14
# #TCS

# import emp as e
# em=int(input("enter basic sal"))#100
# print(e.cal(em))#120.0

# import myvariable
# import mymath
# print(mymath.add(10,20))
# print(myvariable.add(10,20))

# from myvariable import add
# from mymath import add
# print(add(10,20))#30 overwrite kr dega yani last in first execution


# import mypackages 
# #init file executed
# print(mypackages.add(10,20))#30
# print(mypackages.rev("welcome"))#emoclew

# from mypackages import mathop,stringop
# print(mathop.add(10,20))
# print(stringop.rev("welcome"))#init mein nahi ho toh direct krlo

from mypackages .mathop import add,mul,sub
from mypackages .stringop import rev,upper
print(add(10,20))
print(rev("welcome"))
