def strongn(n):
    t=0
    temp=n
    for i in range(len(str(n))):
        a=n%10
        v=1
        for i in range(1,a+1):
            v=i*v
        t+=v
        n=n//10
    if t==temp:
        return "strong"
    else:
        return "not strong "