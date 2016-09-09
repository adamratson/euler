sum = 0
squaresum = 0

for num in range(1, 101):
    sum += num
    squaresum += num * num
sumsquare = sum * sum

diff = sumsquare - squaresum
print(sumsquare)
print(squaresum)
print(str(diff))
