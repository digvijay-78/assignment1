"""12.
=========================================
ONLINE FOOD DELIVERY ANALYSIS
=============================
orders = [
"Pizza",
"Burger",
"Pizza",
"Pasta",
"Burger",
"Pizza",
"Pasta"
]
Write a program to:
* Count orders of each food item.
* Find the most ordered item.
Sample Output:
Pizza : 3
Burger : 2
Pasta : 2
Most Ordered : Pizza"""
orders = [
"Pizza",
"Burger",
"Pizza",
"Pasta",
"Burger",
"Pizza",
"Pasta"
]
d={}
for item in orders:
    d[item]=d.get(item,0)+1
m=max(d.values())
for k,v in d.items():
    print(k,":",v)
for k, v in d.items():
    if m==v:
        print("Most Ordered :",k)