def spy(n):
    s=0
    p=1
    for i in n:
        s+=int(i)
        p=int(i)*p
    if s==p:
        return "spy"
    else:
        return "not spy"