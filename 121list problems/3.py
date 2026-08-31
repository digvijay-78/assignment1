#Remove Element
nums = [3,2,2,3]
s=[]
k=3
for i in range(len(nums)):
    if nums[i] != k:
        s.append(nums[i])
for i in range(len(s)):
    nums[i] =s[i]
print(len(s))















'''    def removeElement(self, nums: List[int], val: int) -> int: 
        s=[]
        for i in range(len(nums)):
            if nums[i] != val:
                s.append(nums[i])
        for i in range(len(s)):'''