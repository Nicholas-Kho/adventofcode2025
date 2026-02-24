with open("day3.txt") as f:
    lines = f.readlines()

total = 0
for l in lines:
    l = l[:len(lines[0])-1]