from math import pow
num = 1000000
numlist = []
numtotal = 0

for x in range(2, num):
    y = 0
    for char in str(x):
        y += pow(int(char), 5)
    if y == x:
        numlist.append(y)
        numtotal += y
print(numlist)
print(numtotal)
