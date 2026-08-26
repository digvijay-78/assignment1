#20Merge Sorted Array
nums1 = [0,1,2,3]
nums2 = [2,5,6]
m = []
n = []
if len(nums2)!=0 and len(nums1)!=0:
    for i in range(len(nums1)):
        if nums1[i]!=0:
            m.append(nums1[i])
        if i<len(nums2) and nums2[i]!=0:
            n.append(nums2[i])
           
res=[]
i=0
j=0
while i<len(m) and j<len(n):
    if m[i]<=n[j]:
        res.append(m[i])
        i+=1
    else:
        res.append(n[j])
        j+=1

if i < len(m):
    res.extend(m[i:])
if j < len(n):
    res.extend(n[j:])
   
print(res)