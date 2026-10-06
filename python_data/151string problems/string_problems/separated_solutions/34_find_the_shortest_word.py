#34Find the shortest word. S = "find the shortest word" "the"
s="find the longest word"
c=s.split()
co=c[0]
for i in c:
    if len(i)<len(co):
        co=i
print("shortest",co)
