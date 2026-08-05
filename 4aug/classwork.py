#unique
#a=[1,2,2,3,4,4,5]
#u=[]
#for i in a:
#    if i not in u:
#        u.append(i)
#print(u)
#
#
#second high
#a=[1,2,2,3,4,4,5]
#u=[]
#for i in a:
#    if i not in u:
#        u.append(i)
#u.sort()
#print(a[-2])

#even odd
# a=[1, 2, 3, 4, 5]
# even=[]
# odd=[]
# for i in a:
    # if i%2==0:
        # even.append(i)
    # else:
        # odd.append(i)
# print(even)
# print(odd)

#common element in a&b
# a=[1,2,3,4,5]
# b=[2,3,4,6,7]
# c=[]
# for i in a:
    # if i in b:
        # c.append(i)
# print(c)

#largest and smallest
a=[1,2,3,4,5,6]
print(max(a))
print(min(a))
l=a[0]
s=a[0]
for i in a:
   if i>l:
       l=i
   if i<s:
      # s=i
print(l)
print(s)

#merge list without duplicates
# a=[1,2,3,4,5,6]
# b=[2,3,4,7,8]
# c=a+b
# result=[]
# for i in c:
    # if i not in result:
        # result.append(i)
# print(result)

#sum at even index 
#a=[1,2,3,4,5,6]
#s=0
#for i in range(0,len(a),2):
#    s = s + a[i]
#print(s)



#reverse without builtin
#a=[1,2,3,4,5,6]
#rev=[]
#new=[]
#for i in range(len(a)-1,-1,-1):
#    rev.append(a[i])
#print(rev)
#
#for i in a:
#    new=[i]+new
#print(new)




#move zero at the end of list
a=[1,2,3,4,5,0,0,1,0,6]
new=[]
non=[]
for i in a:
    if i==0:
        non.append(i)
    else:
        new.append(i)
b=new+non
print(b)
