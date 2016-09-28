import math

x = math.factorial(100)
y = 0
for char in str(x):
    y += int(char)

print(str(y))
