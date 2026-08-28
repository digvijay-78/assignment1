#89Remove 'b' and 'ac' from a string. S = "abacbb" "c"
s=input("enter the string")
remove=input("enter the remove item")
res=""
i=0
while i<len(s):
    ch=s[i]
    if len(remove)==1 and ch==remove :
        i+=1
    elif len(remove)==2 and (i>0 and s[i-1]+s[i]==remove) or (i<len(s)-1 and s[i]+s[i+1]==remove) :
        i+=2
    else:
        res+=ch
        i+=1
print(res)