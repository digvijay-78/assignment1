#15 Third Maximum Number
num = [3,2,2,1]
nums=set(num)
a=0
if len(nums)<=2:
    print(max(nums))
else:
    c=max(nums)
    nums.remove(c)
    nums.remove(max(nums))
    a=max(nums)
    print(a)