#5 Plus One
digits = [1,2,3]
s=""
for i in digits:
    s+=str(i)
r=int(s)+1
t=str(r)

res=[]
for i in t:
    res.append(int(i))
print(res)