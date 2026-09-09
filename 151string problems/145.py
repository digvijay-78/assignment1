#145Remove HTML tags from a string. 
# S = "<h1>Title</h1>" "Title"
s=input("<h1>Title</h1>")
res=""
r=False
for i in range(len(s)):
    if s[i]=="<":
        r=True
    if r==False:
        res+=s[i]
    if s[i]==">":
        r=False

print(res)