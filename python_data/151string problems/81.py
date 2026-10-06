#81Generate a hash code or UUID. S = "test"
#  Hash: 3556498 (Example hash code)

s=input("enter ")
h=0
for ch in s:
    h=h*31+ord(ch)
print(h)
print(ord("t"))
print(ord("e"))
print(ord("s"))
print(ord("t"))