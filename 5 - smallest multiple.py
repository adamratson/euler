import math

divnums = range(2,20)
for num in range(1, 10000000000):
    correct = True
    for divnum in divnums:
        if num % divnum != 0:
            correct = False
            break
    if correct is True:
        print(str(num))
        break
