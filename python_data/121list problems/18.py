#18Shortest Unsorted Continuous Subarray
nums = [2,6,4,8,10,9,15]
a=sorted(nums)
if nums==a:
        print(0)
else:
    c=0
    for i in range(len(nums)):
            if nums[i]!=a[i]:
                    c=i
                    break
    d=0
    for j in range(len(nums)):
            if nums[j]!=a[j]:
                    d=j
    final=(d-c)+1
    print(final)