def d(n):
    divisors = []
    for x in range(1,n):
        if n % x == 0:
            total += x
            divisors.append(x)
    return divisors

for divisor in divisors:
    divdivs = d(divisor)
    x = 0
    divisorsum = sum()
    if sum(d(divisor))
