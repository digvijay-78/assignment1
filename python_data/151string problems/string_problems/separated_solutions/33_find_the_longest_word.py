#33Find the longest word. S = "find the longest word" "longest"

s="find the longest word"
c=s.split()
co=c[0]
for i in c:
    if len(i)>len(co):
        co=i
print("longest Word :",co)
