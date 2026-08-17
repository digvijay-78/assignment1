#67Count how many times a substring appears. S = "abab", Sub = "ab" 2
s=input("")
sub=input("")
c=0
for i in range(len(s)):
    if s[i:i+(len(sub))]==sub:
        c+=1
print(c)





s = input("aaaa")
sub = input("aa")

c = 0
i = 0

while i <= len(s) - len(sub):
    if s[i:i+len(sub)] == sub:
        c += 1
        i += len(sub)      # match ke baad jump
    else:
        i += 1

print(c)