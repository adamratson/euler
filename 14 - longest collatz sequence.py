def collatz(num):
    if num == 1:
        return 1
    if num % 2 == 0:
        return num/2
    else:
        return 3 * num + 1

longest = 1
longestcount = 1

for num in range(1, 1000000):
    done = False
    count = 1
    newnum = collatz(num)
    while done is False:
        newnum = collatz(newnum)
        if newnum == 1:
            done = True
        count += 1
    if count > longestcount:
        longest = num
        longestcount = count

print(longest)
