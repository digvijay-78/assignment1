#19Missing Number
nums = [3,0,1]
a=sorted(nums)
s=0
for i in range(len(a)):
    if abs(a[i-1]-a[i])==1:
        s=a[i]+1
print(s)



# 19 Missing Number
nums = [3, 0, 1]
a = sorted(nums)
s = 0
if a[0] != 0:
    s = 0
else:
    for i in range(1, len(a)):
        if a[i] - a[i-1] != 1:
            s = a[i-1] + 1
            break
    else:
        s = len(a)
print(s)