#10 . Move Zeroes
nums = [0,1,0,3,12]
non=[]
zero=[]
for i in nums:
    if i==0:
        zero.append(i)
    else:
        non.append(i)
print(non+zero)