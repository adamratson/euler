numlendict = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:9, 19:8,
              20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6}

totalcharcount = 0

for num in range(1,1001):
    charcount = 0

    if num in numlendict:
        charcount += numlendict[num]
    elif len(str(num)) == 2:
        charcount += numlendict[int(str(num)[0]+'0')]
        charcount += numlendict[int(str(num)[1])]
    elif len(str(num)) == 3:
        charcount += numlendict[int(str(num)[0])]
        charcount += len('hundred')
        if int(str(num)[1]) != 0 or int(str(num)[2]) != 0:
            charcount += len('and')
        if num == 115:
            print(numlendict[int(str(num)[0])])
            print(numlendict[int(str(num)[1]+'0')])
            print(numlendict[int(str(num)[2])])
        charcount += numlendict[int(str(num)[1]+'0')]
        charcount += numlendict[int(str(num)[2])]
    elif len(str(num)) == 4:
        charcount += numlendict[int(str(num)[0])]
        charcount += len('thousand')
        charcount += numlendict[int(str(num)[1])]
        if int(str(num)[1]) != 0:
            charcount += len('hundred')
        if int(str(num)[2]) != 0 or int(str(num)[3]) != 0:
            charcount += len('and')
        charcount += numlendict[int(str(num)[2]+'0')]
        charcount += numlendict[int(str(num)[3])]

    if num == 115:
        print(charcount)

    totalcharcount += charcount

    """
    charcount = 0
    if num in numlendict.values():
        charcount += numlendict[num]
    elif len(str(num)) == 2:
        charcount += numlendict[int(str(num)[0]+'0')]
        if str(num)[-1] != '0':
            charcount += numlendict[int(str(num)[-1])]
    elif len(str(num)) == 3:
        charcount += len('hundred')
        charcount += numlendict[int(str(num)[0])]
        charcount += numlendict[int(str(num)[1]+'0')]
        if str(num)[-1] != '0':
            charcount += numlendict[int(str(num)[-1])]
    elif len(str(num)) == 4:
        charcount += numlendict[int(str(num)[0])]
        charcount += len('thousand')
        charcount += len('hundred')
        charcount += numlendict[int(str(num)[1])]
        charcount += numlendict[int(str(num)[2]+'0')]
        if str(num)[-1] != '0':
            charcount += numlendict[int(str(num)[-1])]
    totalcharcount += charcount
    """
print(totalcharcount)