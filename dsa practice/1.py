#max consicative 1's atmost flip ==k flip =>{0=1}
#can convert it into max subarry with atmost k =>0's
# arr=[1,1,1,0,0,0,1,1,1,1,0]
# k=2
# l=0
# r=0
# maxl=0
# zero=0
# while r < len(arr):
#     if arr[r]==0:
#         zero+=1
#     while zero>k:
#         if arr[l]==0:
#             zero-=1
#         l+=1
#     if zero<=k:
#         le=r-l+1
#         maxl=max(maxl,le)
#     r+=1
# print(maxl)




# #optimized version.
# arr=[1,1,1,0,0,0,1,1,1,1,0]
# k=2
# l=0
# r=0
# maxl=0
# zero=0
# while r < len(arr):
#     if arr[r]==0:
#          zero+=1
#     if zero>k:
#         if arr[l]==0:
#               zero-=1
#         l+=1   
#     if zero<=k:
#          le=r-l+1
#          maxl=max(maxl,le)
#     r+=1
# print(maxl)


#FRUIT INTO BASKET 
#MAX LEN SUB ARRAY WITH ATMOST 2 TYPES OF FRUITS
#arr=[3,3,3,1,2,1,1,2,3,3,4]



#longest substring with atmost k distinct char
 