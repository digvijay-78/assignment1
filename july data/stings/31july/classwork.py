marks=[10,2,30]
student=['abc','xyz','www']
name=input("enter stu name")
if name in student:
    index=student.index(name)
    newmarks=int(input("enter stu new marks  ="))
    marks[index]=newmarks
else:
    print("not foud")
print(student)
print(marks)



student=['abc','xyz','www']
name=input("enter stu name")
if name in student:
    student.remove(name)
else:
    print("item not found")
print(student)