arange = range(100, 999)
brange = range(100, 999)
final = 0

for a in arange:
    for b in brange:
        c = a * b
        if str(c) == str(c)[::-1]:
            if c > final:
                final = c

print(str(final))