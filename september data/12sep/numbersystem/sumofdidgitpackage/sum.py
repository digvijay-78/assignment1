def su(n):
    res=0
    for i in range(len(str(n))):
        s=n%10
        res+=s
        n=n//10
    return res