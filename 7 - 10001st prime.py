targetprime = False
testprime = 1
numofprimes = 0

while targetprime is False:
    testprime += 1
    prime = True
    for num in range(2,testprime):
        if testprime % num == 0:
            prime = False
            break
    if prime is True:
        numofprimes += 1
        if numofprimes == 10001:
            targetprime = True

print(str(testprime))
