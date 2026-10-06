def harsh(n):
    s=0
    for i in n:
        s+=int(i)
    if int(n)%s==0:
        return "harshad no."
    else:
        return "not"