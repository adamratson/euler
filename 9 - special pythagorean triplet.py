for a in range(1,997):
    for b in range(1,997):
        for c in range(1,997):
            if a + b + c == 1000:
                if (a * a) + (b * b) == c * c:
                    print(str(a*b*c))
                    raise Exception
