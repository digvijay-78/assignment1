#80Print list items containing all characters of a given word. 
# List = ["apple", "plea"], Word = "pal" "apple", "plea"

s=["apple","plea","usdhisner"]
word="pal"
res=[]

for i in range(len(s)):
    c=True
    for j in word:
        if j not in s[i]:
            c=False
            break
    if c and s[i] not in res:
            res.append(s[i])

print(res)