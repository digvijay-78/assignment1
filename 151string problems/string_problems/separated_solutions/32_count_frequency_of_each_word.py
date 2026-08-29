#32Count frequency of each word. S = "apple banana apple" apple: 2, banana: 1

s="apple banana apple"
a=s.split()
b=set(a)
for i in range(len(a)):
    c=0
    v=a[i]
    for j in range(len(a)):
        if v==a[j]:
            c+=1
    print(v,":",c)

for i in b:
    print(i,a.count(i))
