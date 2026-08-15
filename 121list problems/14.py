#14Find the Difference of Two Arrays
nums1 = [1,2,3]
nums2 = [2,4,6]
n=set(nums1)
m=set(nums2)
b=(list(n-m))
c=list(m-n)
d=[]
d.append(b)
d.append(c)
print(d)

#print([list(n-m), list(m-n)])
