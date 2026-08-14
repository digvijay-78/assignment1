#Remove Duplicates from Sorted Array
nums = [1,1,2]
s=[]
for i in range(len(nums)):
    if nums[i] not in s:
        s.append(nums[i])
        
for i in range(len(s)):
    nums[i] =s[i]

print(len(s))



'''class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=[]
        for i in range(len(nums)):
            if nums[i] not in s:
                s.append(nums[i])
        for i in range(len(s)):
            nums[i] =s[i]
        return len(s)'''