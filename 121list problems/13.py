#13Find All Numbers Disappeared in an Array 
arr= [4,3,2,7,8,2,3,1]
for i in range(len(arr)-1):
         if arr[i+1]-arr[i]!=1: 
            print("Missing Value =", arr[i] + 1) 
            break