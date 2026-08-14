#updating 
'''s={10,20,30}
s.update(50)
print(s)#error

s={10,20,30}
s.update([50])
print(s)

s={10,20,30}
s1=s

print(id(s))
print(id(s1))
s2=s.copy()
print(id(s))
print(id(s2))



a={1,2,3,4}
b={3,4,5}
print(a|b)
print(a.union(b))

l1=["yash","gaduyaw","ajay"]
l2=["yash","fuywgi","sahil"]

s=set(l1)
b=set(l2)
z=s.union(b)
l=list(z)

a={1,2,3}
b={2,3,4}
print(a&b)
print(a.intersection(b))


math=["yash","gaduyaw","ajay"]
science=["yash","fuywgi","sahil"]
m=set(math)
s=set(science)
print(m&s)
print(m.intersection(s))

a={1,2,3}
b={2,4}
print(b-a)
print(b.difference(a))

math={"yash","gaduyaw","ajay"}
science={"yash","fuywgi","sahil"}
print(math-science)
print(math.difference(science))
print(science-math)


math={"yash","gaduyaw","ajay"}
science={"yash","fuywgi","sahil"}
print(math^science)
print(math.symmetric_difference(science))
print(science^math)

a={1,2}
b={1,2,3,4}
print(a<=b)
print(a.issubset(b))
print(b.issubset(a))



req={"java","react","mysql"}
can={"java","react","mysql","ml"}
print(req<=can)


b={1,2,3,4}
a={1,2}
print(b>=a)
print(b.issuperset(a))


a={1,2}
b={3,4}
print(a.isdisjoint(b))


a={1,2,3}
b={3,4,5}
a|=b
a.update(b)
print(a)#{1, 2, 3, 4, 5}



a={1,2}
b={3,4}

print(a.isdisjoint(b))

a={1,2,3,4}
b={3,4,5,6}
a.intersection_update(b)
a&=b
print(a)


a={1,2,3,4}
b={3,4}
a.difference_update(b)
a-=b
print(a)
'''
a={1,2,3,4}
b={3,4,5}
a^=b
print(a)


a={1,"hello",(2,3)}
print(a)

#b={1,"hello",[2,3]}
#print(b)