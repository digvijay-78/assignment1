#79Divide a string into n equal parts. 
# S = "abcdef", n = 3 "ab", "cd", "ef"
s="abcdef"
n=3
v=len(s)//n
x=[]
for i in range(len(s)):
    if i%v==0:
        x.append(s[i:i+v])

print(x)