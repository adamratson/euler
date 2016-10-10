from math import sqrt, ceil
from collections import Counter

found = False
count = 1
tri = 0

while found is not True:
    tri += count
    
    divnum = 1

    for num in range(2, ceil(sqrt(tri))):
        if tri % num == 0:
            divnum += 2

    if divnum > 500:
        found = True
    
    count += 1

print(tri)
                                  
"""
while found is not True:
    tri += count
    factnum = 2
    
    if factnum > 5:
        found = True
    count += 2
    
print(tri)
"""
