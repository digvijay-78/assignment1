#3Sum Closest
# Given an integer array nums of length n and an integer target, find three integers at distinct indices in 
# nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.
# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).


nums =[-1,2,1,-4]
targets=1
nums.sort()
s = []
for i in range(len(nums)):
    j = i + 1
    k = len(nums) - 1
    while j < k:
        total = nums[i] + nums[j] + nums[k]
        if total == targets:
            s.append([nums[i], nums[j], nums[k]])
            j += 1
            k -= 1
        elif total < 0:
            j += 1

        else:
            k -= 1
print(s)