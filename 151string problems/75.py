# #75Find the longest common prefix among strings. 
# # Strings = ["flower", "flow", "flight"] "fl"
# s=input("").split()
# prefix=s[0]
# for i in range(1,len(s)):
#     word = s[i]
#     j=0
#     while j < len(word) and j < len(prefix):
#         if word[j] != prefix[j]:
#             prefix = word[:j]
#         else:
#             j+=1

# print(prefix)

s=input("").split()
prefix=s[0]
for i in range(len(s)):
    word=s[i]
    j=0
    while j<len(word) and j<len(prefix):
        if word[j] != prefix[j]:
            prefix=word[:j]
        else:
            j+=1
print(prefix)
