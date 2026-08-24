#21 3Sum [[-1,-1,2],[-1,0,1]]

nums = [-1,0,1,2,-1,-4]
s=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
               if  nums[i] + nums[j] + nums[k] == 0:
                   v=nums[i],nums[j],nums[k]
                   v=sorted(v)
                   if v not in s:
                       s.append(v)
print(s)








nums = [-1, 0, 1, 2, -1, -4]
nums.sort()
s = []
for i in range(len(nums)):
    j = i + 1
    k = len(nums) - 1
    while j < k:
        total = nums[i] + nums[j] + nums[k]
        if total == 0:
            s.append([nums[i], nums[j], nums[k]])
            j += 1
            k -= 1

        elif total < 0:
            j += 1

        else:
            k -= 1

print(s)