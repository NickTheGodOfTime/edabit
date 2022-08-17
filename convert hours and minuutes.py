def convert(h, m):
  return (h * 3600) + m * 60

e = convert(1, 3)
print(e)
e = convert(2, 0)
print(e)
e = convert(0, 0)
print(e)