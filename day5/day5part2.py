with open("day5.txt") as f:
    lines = f.read()

def mergeFirstRange(ranges):
    l = ranges[0][0]
    r = ranges[0][1]
    print(ranges)
    while True:
        for i in range(1, len(ranges)):
            replace = False
            if r >= ranges[i][0] >= l:
                ranges[i][0] = l
                if l <= ranges[i][1] <= r:
                    ranges[i][1] = r
                replace = True
            elif l <= ranges[i][1] <= r:
                ranges[i][1] = r
                if r >= ranges[i][0] >= l:
                    ranges[i][0] = l
                replace = True
            elif (l <= ranges[i][0] and r >= ranges[i][1]):
                ranges.pop(i)
                ranges.insert(0, (l, r))
                return ranges
            elif (ranges[i][0] <= l and ranges[i][1] >= r):
                ranges.pop(0)
                return ranges
            if replace:
                t = ranges.pop(i)
                ranges.pop(0)
                ranges.insert(0, t)
                return mergeFirstRange(ranges)
        return ranges

ranges = lines.split("\n\n")[0]
unique = []
for r in ranges.split("\n"):
    l = int(r.split("-")[0])
    r = int(r.split("-")[1])
    unique.insert(0, [l, r])
    unique = mergeFirstRange(unique)

total = 0
for r in unique:
    total += r[1]-r[0] + 1
print(total)
print(unique)