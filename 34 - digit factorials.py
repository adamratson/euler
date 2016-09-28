from math import factorial

top = 1000000
total = 0
for num in range(3, top):
    x = 0
    for char in str(num):
        x += factorial(int(char))
    if x == num:
        total += x

print(total)
        
