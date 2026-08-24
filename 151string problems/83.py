#83Create a string from a byte array.
#  Byte[] = {72, 101, 108} (ASCII for H, e, l) "Hel"
c=[72,101,108]
res=""
for i in c:
    res+=chr(i)
print(res)

r=[chr(i) for i in c]
print(r)