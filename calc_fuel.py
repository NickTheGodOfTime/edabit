def calculate_fuel(fuel):
  return max(fuel * 10, 100)


e = calculate_fuel(15)
print(e)
e = calculate_fuel(23.5)
print(e)
e = calculate_fuel(3)
print(e)