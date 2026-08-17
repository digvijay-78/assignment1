#53Remove punctuation. S = "Hello, world!" "Hello world"
s="hello world"
z=""
for i in s:
    if ("a"<=i<="z") or ("A"<=i<="Z"):
        z+=i
    elif ("0"<=i<="9") or i==" ":
        z+=i
print(z)