#147Decompress a run-length encoded string. 
# S = "a3b2c1" "aaabbc"
s=input("enter the string")
res=""
for i in range(len(s)):
    if s[i].isdigit():
        v=int(s[i])-1
        res=res+(s[i-1])*v
    elif s[i-1].isdigit() and s[i].isdigit():
        res+=s[i]
    else:
        res+=s[i]
print(res)