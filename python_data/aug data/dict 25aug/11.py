"""
11.
=========================================
PRODUCT SALES ANALYSIS
======================
sales = [
"Mobile",
"Laptop",
"Mobile",
"Tablet",
"Laptop",
"Mobile"
]
Write a program to:
* Count sales of each product.
* Display products in sorted order.
Sample Output:
Laptop : 2
Mobile : 3
Tablet : 1"""

sales = [
"Mobile",
"Laptop",
"Mobile",
"Tablet",
"Laptop",
"Mobile"
]
d={}
for product in sorted(sales):
    d[product]=d.get(product,0)+1
print(d)

for k, v in d.items():
    print(k, ":", v)