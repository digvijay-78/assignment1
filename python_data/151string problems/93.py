#93Match strings with wildcard characters ($\*$, ?). 
# Pattern = "a?c", Text = "axcde" TRUE

p="a?c"
text="axcde"
i=0
j=0
c=0
while j<len(text) and i<len(p):
    if p[i]==text[j]:
        i+=1
        j+=1
    elif p[i]=="?":
            i+=1
            j+=1
    else:
         break
    if i==len(p):
         c=1
print(c)