# 57Merge two strings alternatively. S1 = "ABC", S2 = "def" "AdBeCf"
# s="ABC"
# s1="def"
# result=""
# for i in range(len(s)):
#     if len(s)!=i:
#         result+=s[i]
#     if len(s1)!=[i]:
#         result+=s1[i]
# print(result)

s = input("Enter first string: ")
s1 = input("Enter second string: ")
result=""
for i in range(max(len(s),len(s1))):
    if i<len(s):
        result += s[i]
    if i<len(s1):
        result += s1[i]

print(result)