#77Find the longest substring that appears at both ends.
#  S = "abracadabra" "abra"
s=input("")
res=""
word=len(s)-1
for i in range(len(s)):
    if s[:word]==s[-word:]:
        res=s[:word]
        break
    else:
        word-=1
if len(res) == 0:
    print("No common substring found")
else:
    print(res)
    