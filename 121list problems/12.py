nums = [-2,1,-3,4,-1,2,1,-5,4]
l=[] 
for i in range(len(nums)): 
    for j in range(i+1,len(nums)+1): 
        l.append(nums[i:j]) 
s=[] 
for i in l: 
    s.append(sum(i)) 
print(max(s)) 