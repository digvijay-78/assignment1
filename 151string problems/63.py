#63Count frequency of each character. S = "aabcc" a: 2, b: 1, c: 2
s="aabcc"
for i in range(len(s)):
    c=0
    for j in range(i,len(s)):
        if s[i]==s[j] and s[i-1]!=s[i]:
            c+=1
    if c!=0:
        print(s[i],":",c)


for i in range(len(s)):
    c=0
    if i>0 and s[i-1]==s[i]:
        continue
    for j in range(len(s)):
        if s[i]==s[j] :
            c+=1
    print(s[i],":",c)
