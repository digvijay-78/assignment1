# import random
# print(random.random())#0.7021466012962337
# print(random.uniform(10,20))#13.92447893932406

# print(random.randint(10,20))#19

# import random
# print(random.randrange(10,20,2))

# import random
# name=["deep","neetudi","virat"]
# print(random.choice(name))#neetudi

# import random
# print(random.choice([True,False]))#True

# import random
# name=["deep","neetudi","virat"]
# print(random.choices(name,k=2))#['virat', 'virat']



# import random
# name=["deep","neetudi","virat"]
# # print(random.sample(name,k=2))#['deep', 'neetudi']

# random.shuffle(name)
# print(name)


# import random
# print("dice rolling")
# dice=random.randint(1,6)
# print("you got",dice)#you got 3

# import random
# import string
# print(string.ascii_letters)
# print(string.digits)
# #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# #0123456789


# import random
# import string
# char=string.ascii_letters+string.digits
# password=random.choices(char,k=8)
# print(password)#['a', 'u', 'q', 'o', 'p', 'c', 'K', 'M']
# password1="".join(random.choices(char,k=8))
# print(password1)#K8vQVw0B

# import random
# n=random.randint(1,10)
# guess=int(input("guess no"))
# if guess==n:
#     print("correct")
# else:
#     print("wrong")

# from datetime import date
# today=date.today()
# print(today)#2026-09-10

# print(today.year)#2026
# print(today.month)#9
# print(today.day)#10


# from datetime import date
# d=date(2025,12,25)
# print(d)#2025-12-25
# print(d.year)#2025
# print(d.month)#12
# print(d.day)#25



# from datetime import datetime
# d=datetime.now()
# print(d)#2026-09-10 14:51:57.506877
# print(d.year)#2026
# print(d.month)#9
# print(d.day)#10
# print(d.min)#0001-01-01 00:00:00
# print(d.second)#56


# from datetime import datetime
# d=datetime(2026,2,20,10,30,00)
# print(d)#2026-02-20 10:30:00
# print(d.year)#2026
# print(d.month)#2
# print(d.day)#20
# print(d.min)#0001-01-01 00:00:00
# print(d.second)#0


# from datetime import datetime
# now=datetime.now()
# print(now)#2026-09-10 14:58:27.086457
# # date=now.strftime("%Y-%m-%d")
# print(date)#2026-09-10

# date=now.strftime("%Y %y %m  %B %b %d %D %M")#M=min
# print(date)#2026 26 09 September Sep 10 09/10/26



# from datetime import datetime
# now=datetime.now()
# date=now.strftime("%H %I %M %S %p ")#I => 12 wale time mein 3 o clock =15 o clock 
# print(date)#15 03 04 27 PM 




# from datetime import datetime
# now=datetime.now()
# date=now.strftime("%A %a %w %j") 
# print(date)#Thursday Thu 4 253


# from datetime import datetime
# d="20-02-2026"
# dt=datetime.strptime(d,"%d-%m-%Y")
# print(dt)#2026-02-20 00:00:00
# print(dt.year)#2026
# print(type(d))#<class 'str'>
# print(type(dt))#<class 'datetime.datetime'>


# from datetime import datetime
# d="15-08-2000"
# dt=datetime.strptime(d,"%d-%m-%Y")
# today=datetime.now()
# print(dt)#2000-08-15 00:00:00
# print(today)#2026-09-10 15:27:35.319918
# age=today.year-dt.year
# print(age)#26

# #WAP to print date after 7 days from now 
# from datetime import datetime,timedelta
# d=datetime.now()
# print(d)#2026-09-10 15:38:11.341564
# day=d+timedelta(7)#2026-09-17 15:37:58.214363
# print(day)


# from datetime import datetime,timedelta
# d1=datetime(2026,5,20)
# d2=datetime(2026,2,10)
# diff=d1-d2
# print(diff.seconds)
# #print(dir(timedelta))
# hour=diff.total_seconds()//3600
# print(hour)#2376.0

#['__abs__', '__add__', '__bool__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', 
# '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__',
#  '__init_subclass__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__',
#  '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__',
#  '__rsub__', '__rtruediv__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', 
# 'days', 'max', 'microseconds', 'min', 'resolution', 'seconds', 'total_seconds']