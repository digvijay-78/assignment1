#137Find the length of the longest substring with at most k distinct characters. 
# S = "eceba", k = 2 3 ("ece")

s="eceba"
mp = {}
k=2
l=0
r=0
maxle=0
while r<len(s):
    mp[s[r]]=mp.get(s[r],0)+1
    if len(mp)>k:
        mp[s[l]]-=1
        if mp[s[l]]==0:
            mp.pop(s[l])
        l+=1
    if len(mp)<=k:
        maxle=max(maxle,r-l+1)
    r+=1
print(maxle)