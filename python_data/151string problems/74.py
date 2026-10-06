#74Find the longest substring without repeating characters. 
# S = "abcabcbb" "abc"
s="abcbdefgh"
a=[]
res=False
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        if len(s[i:j])==len(set(s[i:j])):
            a.append(s[i:j])
max=0
m=""
for i in a:
    if len(i)>max:
        max=len(i)
        m=i
print(m)