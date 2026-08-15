#7 Single Number
nums = [2,2,1]
c=0
for i in nums:
    if nums.count(i)==1:
        c=i
print(c)



c = 0
for i in nums:
    c = c ^ i
print(c)