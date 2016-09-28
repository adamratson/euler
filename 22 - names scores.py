f = open("p022_names.txt", mode='r')

namelist = str(f.read().replace('"', '')).split(',')
namelist = sorted(namelist)

charscores = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'J':10,
              'K':11, 'I':9, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17,
              'R': 18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25,
              'Z':26}

count = 0
total = 0
for name in namelist:
    namescore = 0
    count += 1
    for char in name:
        namescore += charscores[char]
    namescore *= count
    total += namescore

print(total)

f.close()
