def auto(n):
    s=int(n)**2
    v=str(s)
    if n==v[-len(n):]:
        return "auto"
    else:
        return "not auto"