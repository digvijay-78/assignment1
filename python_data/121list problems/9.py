# 9Intersection of Two Arrays 2
nums1 = [1,2,2,1]
nums2 = [2,2]
c=[]
for i in range(len(nums1)):
    for j in range(len(nums2)):
        if nums1[i]==nums2[j]:
            c.append(nums2[j])
            break
print(c)




nums1 = [1,2,2,1]
nums2 = [2,2]
c=[]
for i in (nums1):
    for j in range(len(nums2)):
        if i ==nums2[j]:
            c.append(i)
            nums2.pop(j)
            break
print(c)
