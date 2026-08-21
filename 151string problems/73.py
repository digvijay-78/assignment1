#73Find the longest palindromic substring.
#  S = "babad" "bab" (or "aba")
s="babad"
a=""
c=0
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        if len(s[i:j])>c:
            if s[i:j]==s[i:j][::-1]:
                a=s[i:j]
                c=len(s[i:j])
print(a)