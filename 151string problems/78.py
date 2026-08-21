#78Find the longest mirror-image substring at both ends. 
# S = "aabccbaa" "aab"
s="aabccbaa"
res=""
word=len(s)-1
for i in range(len(s)):
    if s[:word]==s[-word:][::-1]:
        res=s[:word]
        break
    else:
        word-=1
if len(res) == 0:
    print("No mirror-image substring found")
else:
    print(res)