#23 Subarray Sum Equals K
# Given an array of integers nums and an integer k, 
# return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.
# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

nums = [1,2,3]
k = 3
l=[] 
for i in range(len(nums)): 
    for j in range(i+1,len(nums)+1): 
        l.append(nums[i:j]) 
c=0

for i in range(len(l)):
    if sum(l[i])==k:
            c+=1
print(c)
