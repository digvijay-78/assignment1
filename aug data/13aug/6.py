"""
6.

NOTE: using tuple only
An electronics store wants to maintain product information. Since product details should not be modified accidentally,
 each product record is stored as a tuple.

Tuple Format:

(product_id, product_name, price)

Requirements:

Read N product details from the user and store them as tuples in a list.
Display all product details.
Find and display the costliest product.
Find and display the cheapest product.
Calculate and display the average price of all products.
Display all products whose price is greater than ₹50,000.

Test Case:

Input:

Enter number of products: 4

P101 Laptop 65000
P102 Mobile 25000
P103 Television 80000
P104 Tablet 30000

Expected Output:

All Products:
('P101', 'Laptop', 65000)
('P102', 'Mobile', 25000)
('P103', 'Television', 80000)
('P104', 'Tablet', 30000)

Costliest Product:
('P103', 'Television', 80000)

Cheapest Product:
('P102', 'Mobile', 25000)

Average Price:
50000.0

Products Above ₹50,000:
('P101', 'Laptop', 65000)
('P103', 'Television', 80000)"""

from collections import namedtuple
product=namedtuple("poduct",["product_id","product_name", "price"])
n=int(input("Enter number of products:"))
a=[]
for i in range(n):
    print("enter details")
    id=input("enter product_id>")
    name=input("enter name")
    price=int(input("enter price"))
    m=product(id,name,price)
    a.append(m)
for i in a:
    t=((i.product_id,i.product_name, i.price))
    print(tuple(t))
c=a[0]
d=a[0]
m=0
for k in a:
    if k.price>c.price:
        c=k
    if k.price>d.price:
        d=k
    m=m+k.price
avg=m/n
print("Costliest Product:\n",tuple(c))
print("Cheapest Product:\n",tuple(d))
print("Average Price:\n",avg)