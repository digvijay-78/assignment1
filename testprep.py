'''# print("a"==97)
# print(None or "deep")


#WAP to add 2 matrix
a=[[2,3],[4,5]]
b=[[8,10],[9,11]]
c=[]
for i in range(len(a)):
    row=[]
    for j in range(len(a[i])):
        row.append(a[i][j]+b[i][j])
    c.append(row)
print("display")
print(*c)'''

nums = [2, 7, 11, 15]
target = 9
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        ch=nums[i]+nums[j]
        if ch==target:
            print(i,j)


s = "aabbcdeef"
for st in s:
    if s.count(st)==1:
        print(st)
        break


nums = [0, 1, 0, 3, 12]
z=0
for i in range(len(nums)):
    if nums[i]!=0:
        nums[z]=nums[i]
        z+=1
for i in range(z, len(nums)):
    nums[i] = 0

print(nums)

nums = [3, 0, 1]
nums.sort()
for i in range(len(nums)-1):
    if  nums[i+1]-nums[i]!=1:
        print(nums[i+1]-nums[i])
        break
else:
    print(nums[-1]+1)