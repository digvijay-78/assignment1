#90Remove adjacent duplicates recursively. S = "azxxzy" "ay"
s=input("enter the string")
while True:
    res=""
    i=0
    while i<len(s):
        if i<len(s)-1 and s[i]==s[i+1]:
            i+=2
        else:
            res+=s[i]
            i+=1

    if res==s:
        break
    s=res
print(res)
