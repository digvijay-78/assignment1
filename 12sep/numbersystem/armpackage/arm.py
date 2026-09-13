def armstrong(n):
    s=int(n)
    t=0
    for i in range(len(n)):
        v=s%10
        c=v**len(n)
        t+=c
        s=s//10
    if t==int(n):
        return "arm"
    else:
        return "not"