#146Compress a string using run-length encoding. 
# S = "aaabbc" "a3b2c1"
s="aaabbc"
res=""
for i in s:
  if i not in res:
    v=s.count(i)
    res+=i+str(v)
  elif i.isdigit():
    res+=i 
print(res)