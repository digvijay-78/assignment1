#10Trim leading, trailing, or extra spaces. S = "  hello  world  " "hello world"
s = "  hello  world  "
result = " ".join(s.split())
print(result)
