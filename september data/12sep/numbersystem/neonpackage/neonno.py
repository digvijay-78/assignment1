def neon(n):
    s=int(n)**2
    m=0
    for i in str(s):
       m+=int(i)
    if str(m)==n:
        return "neon"
    else:
        return "not neon" 