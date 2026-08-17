#41Check if a string contains a substring (without using built-in method). 
# #S1 = "Hello", Sub="ell" TRUE

s="hello"
sub="ell"
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        if s[i:j]==sub:
            print("true")
            break
else:
    print("False")

for i in range(len(s) - len(sub) + 1):
    if s[i:i+len(sub)] == sub:
        print("True")
        break
else:
    print("False")

