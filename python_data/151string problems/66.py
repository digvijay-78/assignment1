#66Count number of sentences in a paragraph. P = "This. Is. Test." 3
p="This. Is. Test."
c=0
for i in range(len(p)):
    if (p[i-1]!=p[i]) and p[i]=="."or p[i]=="?" or p[i]=="!":
        c+=1
print(c)


p = "heloo....  how are you? i am fine."
c = 0

for i in range(len(p)):
    if p[i] in ".?!":
        if i == 0 or p[i-1] != p[i]:
            c += 1

print(c)