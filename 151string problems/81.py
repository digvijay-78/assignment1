#81Generate a hash code or UUID. S = "test"
#  Hash: 3556498 (Example hash code)

s="test"
h=0
for ch in s:
    h=h*31+ord(ch)
print(h)
print(ord("t"))