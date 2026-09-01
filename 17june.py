rows1=int(input("enter the no of rows "))
col1=int(input("enter the no of col "))
m=[]
for i in range( rows1):
    row=[]
    for j in range(col1):
        row.append(int(input()))
    m.append(row)


r2=int(input("enter rows for sec matrix"))
c2=int(input("enter col for sec matrix"))
print("enter elements for sec matrix")
B=[]
for i in range(r2):
    row=[]
    for j in range(c2):
        row.append(int(input()))
    B.append(row)
res=[]
if col1==r2:
    for i in range(rows1):
        row=[]
        for j in range(c2):
            row.append(0)
        res.append(row)
    for i in range(rows1):
        for j in range(c2):
            for k in range(col1):
                res[i][j]=res[i][j]+m[i][k]*B[k][j]
    print("result is ")
    print(*res)
else:
    print("Matrix multiplication is not possible")



s = input("")
s1 = input("")
i = 0
j = 0
c = 0
while i < len(s) and j < len(s1):
    if s[i] != s1[j]:
        c += 1
        if len(s) > len(s1):
            i += 1
        elif len(s) < len(s1):
            j += 1
        else:
            i += 1
            j += 1
    else:
        i += 1
        j += 1
if i < len(s) or j < len(s1):
    c += 1
if c == 1:
    print(True)
else:
    print(False)


from collections import namedtuple

player=namedtuple("player",["player_id","player_name","runs"])

n=int(input("enter no of players =>"))
p=[]

for i in range(n):
    print("enter details")
    id=int(input("enter player.id>"))
    name=input("enter name")
    runs=int(input("enter runs"))
    s=player(id,name,runs)
    p.append(s)

print("details")
for x in p:
    print(x.player_id,x.player_name,x.runs)

c=p[0]
for y in p:
    if y.runs>c.runs:
        c=y
print("Highest Scorer:")
print(c.player_id,c.player_name,c.runs)

d=p[0]
for y in p:
    if y.runs<d.runs:
        d=y
print("Lowest Scorer:")
print(d.player_id,d.player_name,d.runs)

m=0
for k in p:
    m=m+k.runs

print("Total Runs:")
print(m)

avg=m/n
print("Average Runs:")
print(avg)

print("Players Scoring More Than 50 Runs:")
for x in p:
    if x.runs>50:
        print(x.player_id,x.player_name,x.runs)


n=["abc", "de", "fg", "ad"] 
c=0
for i in range(len(n)):
    for j in range(i+1,len(n)):
        s=n[i]+n[j]
        x=0

        for k in s:
            if s.count(k)>1:
                 x=1
                 break
        if x==0:
            print(n[i],n[j])
            c+=1    
print(c)






strings = ["baking", "making", "taking"] 

strings.sort()

first = strings[0]
last = strings[-1]

i = 0

while i < len(first) and i < len(last) and first[i] == last[i]:
    i += 1

j=-1
k=0
while k < len(first) and k < len(last) and first[j] == last[j]:
    j -= 1
    k+=1

print(first[j+1:])