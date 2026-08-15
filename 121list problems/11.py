#11 . Best Time to Buy and Sell Stock
prices = [7,6,4,3,1]
prices = [7,1,5,3,6,4]
c=[0]
for i in range(len(prices)):
    for j in range(i+1,len(prices)):
        if prices[i]<prices[j]:
            cd=abs(prices[i]-prices[j])
            c.append(cd)
        

print(max(c))