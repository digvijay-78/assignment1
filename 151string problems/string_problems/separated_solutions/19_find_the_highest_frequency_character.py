#19Find the highest frequency character. S = "abracadabra" a'
s="abcdsesaaaqaaa"
a=""
c=0
for i in s:
    b=s.count(i)
    if b>c :
        c=b
        a=i
print(a,c)
