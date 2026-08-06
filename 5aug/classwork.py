"""WAP peak elemnt index"""
'''
n=int(input("size"))
arr=[]
for i in range(n):
    arr.append(int(input()))
p=-1
for i in range(n):
    if i==0:
        if n==1 or arr[i]>arr[i+1]:
            p=i
            break
    elif i==n-1:
        if arr[i]>=arr[i-1]:
            p=i
            break
    else:
        if arr[i]>=arr[i-1] and arr[i]>=arr[i+1]:
                p=i
                break
if p!=-1:
     print("peak index",p)
     print("peak index",arr[p])
else:
     print("not found")
'''


'''WAP sum of leaders '''
n=int(input("size"))
if n==0:
     print(-1)
else:
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    leadersum=0
    for i in range(n):
         isleader=True
         for j in range(i+1,n):
              if arr[i]<=arr[j]:
                   isleader=False
                   break
         if isleader:
            leadersum+=arr[i]
    print("sum is ",leadersum)