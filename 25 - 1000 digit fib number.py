def fib(n):
    nextn = fibnums[-2] + fibnums[-1]
    fibnums.append(nextn)
    return str(nextn)

fibnums = [1, 1]
n = '1'
while len(n) < 1000:
    n = fib(int(n))
print(len(fibnums))
