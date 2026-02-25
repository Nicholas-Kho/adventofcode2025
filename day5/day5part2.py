with open("day5.txt") as f:
    lines = f.read()

ranges = lines.split("\n\n")[0]
unique = []
for r in ranges.split("\n"):
    l = int(r.split("-")[0])
    r = int(r.split("-")[1])
    for range in unique:
        if (r >= range[1]):
            range[0] = l
        if (l <= range[0]):
            range[1] = r

def mergeRange(coord, ranges):
    l = coord[0]
    r = coord[1]

    if (r > range[1]):
        range[0] = l
    if (l <= range[0]):
        range[1] = r
