'''
 5. Social Media Hashtag Trend Window

A social media company wants to analyze the smallest substring containing all unique characters from a hashtag.

### Input:

text
aabcbcdbca


### Output:

text
dbca
'''
n=input("=")
c=""
for i in range(len(n)):
    if n[i]!=n[i-1] and c in n:
        c=c+n[i]
print(c)