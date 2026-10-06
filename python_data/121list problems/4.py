#Search Insert Position
# nums = [1,3,5,6]
# target = 5
# l=0
# r=len(nums)-1
# mid=0
# while l<=r:
#     mid=(l+r)//2
#     if nums[mid]==target:
#         print( mid)
#         break
#     elif nums[mid] <target:
#         l=mid+1
#     else:
#         r=mid-1
# print(l)


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l=0
        r=len(nums)-1
        mid=0
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] <target:
                l=mid+1
            else:
                r=mid-1
        return l
