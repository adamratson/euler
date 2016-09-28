import itertools

x = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
y = ['0', '1', '2']

millionth = itertools.permutations(x)
count = 0
for item in millionth:
    count += 1
    if count == 1000000:
        print(item)
    
