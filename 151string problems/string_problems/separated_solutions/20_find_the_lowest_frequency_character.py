#20Find the lowest frequency character. S = "aabbcde" c', 'd', 'e' (any one or all)
s="abcdsesaaaqaaa"
a=""
c=len(s)
for i in s:
    b=s.count(i)
    if b<c :
        c=b
        a=i
print(a,c)
