#65Count palindromic substrings. S = "aaa" 6 (a, a, a, aa, aa, aaa)
s="aaa"
c=0
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        v=s[i:j]
        if s[i:j]==v[::-1]:
            c+=1
print(c)