#54Replace duplicate chars with '$'. S = "hello" "he$lo"
s="hello"
z=""
for i in range(len(s)):
    if i < len(s)-1 and s[i]==s[i+1]:
        z+="$"
    else:
        z+=s[i]
print(z)

s="hello"
z=""

for i in range(len(s)):
    if i >0 and s[i-1]==s[i]:
        z+="$"
    else:
        z+=s[i]

print(z)

