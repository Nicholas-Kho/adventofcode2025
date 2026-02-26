with open("day6.txt") as f:
    lines = f.readlines()
comps = []


for l in lines:
    c = 0
    print(l)
    l = l.split(" ")
    l[len(l)-1] = l[len(l)-1].strip()
    r = []
    for i in range(len(l)):
        c += len(l[i])
        if l[i] == '':
            r.append(i - len(r))
        l[i] = l[i].strip()
        print(c, l[i], "test", len(l[i]), i)
        lmost = lines[1][c - len(l[i])] == ' '
        print(lmost)
        c += 1
    for i in r:
        l.pop(i)

    comps.append(l)


def checkColumn(comps, index):
    r = len(str(comps[0][index]))
    t = 0
    for x in range(r):
        s = ""
        for i in range(0, len(comps)-1):
            #print(len(comps[i][index]), "-=-=-", x)
            if len(comps[i][index]) > x:
                #print(comps[i][index], r, x, i, comps[i][index][x])
                s += comps[i][index][len(comps[i][index])-x-1]
        #print(s)
        match comps[len(comps)-1][index]:
            case '*':
                t += 1 if t == 0 else 0
                t *= int(s)
            case '+':
                t += int(s)
    #print(t)
    return t

#print(checkColumn(comps, 1), "asdasd")

l = len(comps) - 1
t = 0
for i in range(len(comps[0])):
    #t += checkColumn(comps, i)
    pass

#print("total :", t)



