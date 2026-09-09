#138Find all palindromic partitions of a string. 
# S = "aab" ["a", "a", "b"], ["aa", "b"]
s="aab"
res=[]
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        if s[i:j]==s[i:j][::-1]:
            if s[i:j] not in res:
                res.append(s[i:j])
print(res)