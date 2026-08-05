#6Convert a string to uppercase. S = "hello" "HELLO
s = "hello"
print(s.upper())



#7Convert a string to lowercase. S = "HELLO" "hello"
s = "hello"
print(s.lower())


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



#9Check whether a string is empty. S1 = "", S2 = "A" S1: True, S2: False
s1 = ""
s2 = "A"

print("S1:", s1 == "")
print("S2:", s2 == "")


#10Trim leading, trailing, or extra spaces. S = "  hello  world  " "hello world"
s = "  hello  world  "
result = " ".join(s.split())
print(result)