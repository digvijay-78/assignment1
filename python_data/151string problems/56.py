#56Reverse only consonants. S = "apple" "alppe"
s="apple"
a=""
for i in range(len(s)):
    if s[i] not in "aeiouAEIOU":
        a+=s[i]
a=a[::-1] 
j=0
result=""
for i in range(len(s)):
    if s[i] not in "aeiouAEIOU":
        result+=a[j]
        j+=1
    else:
        result+=s[i]

print(result)

