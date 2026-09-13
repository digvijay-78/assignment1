def perfectn(number):
    t=0
    for i in range(1,number//2+1):
        if number%i==0:
            t+=i
    if number==t:
        return "prefect"
    else:
        return " not"