#76Find the longest common suffix among strings.
#  Strings = ["baking", "making", "taking"] "king"
s=["baking", "making", "taking"] 
suffix=s[0][::-1]
for i in range(len(s)):
    word=s[i][::-1]
    j=0
    while j<len(word) and j<len(suffix):
        if word[j]!=suffix[j]:
            suffix=word[:j]
        else:
            j+=1
print(suffix[::-1])