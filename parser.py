def toFloat(x):
    return [float(i) for i in x]

def fortyTwo(x):
    return toFloat([x == 1, x == 2, x == 3, x == 4, x == 5, x == 6, x == 7, x == 8, x == 9])

def sixty(x):
    return [x/15.]

def sixtyEight(x):
    return [(x-18.)]

def nintySix(x):
    if x == '':
        return [1]
    return [float(int(x) == 2)]

def one0one(x):
    if x == '':
        return [1]
    return [float(int(x) == 2)]

def oneSixteen(x):
    if x == 99:
        return [0]
    return [x/14.]

def oneTwoOne(x):
    if x == '':
        return [0]
    return [(int(x)-14)/96.]

def school(x):
    return [(x-1)/13.]

def oneSevenSeven(x):
    return toFloat([x == '1', x == '2', x == '3', x == '4', x == '5', x == '6', x == '7', x == '8', x == ''])

def twoThirty(x):
    return [float(x-1)]

def two3743(x):
    return toFloat([x == 1, x == 2, x == 3, x == 4, x >= 5])

def three142(x):
    return [float(x>1)]

def three152(x):
    return [float(x>1)]

def three198(x):
    return [float(x>1)]

def three206(x):
    return [float(x>1)]

def three228(x):
    return [float(x>1)]

def three230(x):
    return [float(x>1)]

def three234(x):
    return [float(x>1)]


def parser(name):
    ret = []
    y = []
    amax = 0
    with open(name, 'r') as f:
        for line in f:
            hold = []
            line = line.split(',')
            hold += fortyTwo(int(line[8]))
            hold += sixty(int(line[19]))
            hold += sixtyEight(int(line[26]))
            amax = max(sixtyEight(int(line[26]))[0], amax)
            hold += nintySix(line[35])
            hold += one0one(line[40])
            hold += oneSixteen(int(line[51]))
            hold += oneTwoOne(line[54])
            hold += school(int(line[59]))
            hold += oneSevenSeven(line[98])
            hold += twoThirty(int(line[122]))
            for i in range(7):
                hold += two3743(int(line[129+i]))
            hold += three142(int(line[2480]))
            hold += three152(int(line[2490]))
            hold += three198(int(line[2536]))
            hold += three206(int(line[2544]))
            hold += three228(int(line[2566]))
            hold += three230(int(line[2568]))
            hold += three234(int(line[2572]))
            ret += hold
            y += [float(line[163]>1)]
        for i in range(len(ret)):
            ret[i][10] /= float(amax)
    return ret, y
    