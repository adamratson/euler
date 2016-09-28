import math
a = 101 
b = 101
numlist = []
for x in range(2, a):
    for y in range(2, b):
        num = math.pow(x, y)
        if num not in numlist:
            numlist.append(num)

print(len(numlist))
