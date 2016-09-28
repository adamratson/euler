from itertools import permutations
top = 1000000
count = 0
x = 2

def isprime(n):
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

def rotate(l, n):
    return l[-n:] + l[:-n]

def rotation(x):
    rotations = []
    count = 1
    for char in str(x):
        rotations.append(int(rotate(str(x), count)))
        count += 1
    return rotations

while x < top:
    prime = False
    circle = False
    if isprime(int(x)):
        circle = True
        perms = rotation(x)
        for num in perms:
            if not isprime(int(num)):
                circle = False
                break
    if circle is True:
        count += 1
    x += 1
print(count)
            
