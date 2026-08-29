#8Toggle the case of each character. S = "MiXED" "mIxeD"
s = "MiXED"
#print(s.swapcase())
result = ""

for ch in s:
    if 'A' <= ch <= 'Z':
        result += chr(ord(ch) + 32)
    elif 'a' <= ch <= 'z':
        result += chr(ord(ch) - 32)
    else:
        result += ch
print(result)
