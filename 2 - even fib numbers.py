prev = 1
curr = 2
fibsum = 2

while curr < 4000000:
    nextnum = prev + curr
    if nextnum % 2 == 0 and nextnum < 4000000:
        fibsum += nextnum
    prev = curr
    curr = nextnum

print(str(fibsum))

