with open("day6.txt") as f:
    lines = f.readlines()
comps = []

for l in lines:
    l = l.split(" ")
    r = []
    for i in range(len(l)):
        if l[i] == '':
            r.append(i - len(r))
        l[i] = l[i].strip()
    for i in r:
        l.pop(i)
    comps.append(l)

total = 0
print(comps[0])
l = len(comps) - 1
for i in range(len(comps[0])):
    sub = int(comps[0][i])
    match comps[l][i]:
        case '*':
            for x in range(1, l):
                sub *= int(comps[x][i])
        case '+':
            for x in range(1, l):
                sub += int(comps[x][i])
    total += sub
print(total)