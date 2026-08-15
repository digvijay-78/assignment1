gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

for i in range(len(gas)):
    t=0
    c=cost[i+1]
    if gas[i]-c<gas[i+1]: