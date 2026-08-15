#8Contains Duplicate
nums = [0,4,5,0,3,6]
# c=0
# for i in nums:
    # c=nums.count(i)
    # if c>=2:
        # break
# if c>=2:
    # print(2)
# else:
    # print(1)


c=0
for i in nums:
    if nums.count(i) >= 2:
        c=1
if c==1:
    print(1)
else:
    print(0)
