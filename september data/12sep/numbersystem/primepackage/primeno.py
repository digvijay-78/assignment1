def prime (n,i=2):
    if n<2:
        return 0
    if i==n:
         return 1
    if n%i==0:
            return 0
    return prime(n,i+1)