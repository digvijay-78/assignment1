
def mini(a,k):
    d=[]
    for i in range(len(a)):
        for j in range(i+1,len(a)+1):
            if sum(a[i:j])==k:
                d.append(a[i:j])
    print(d[1])



