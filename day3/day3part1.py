with open("day3.txt") as f:
    lines = f.readlines()

total = 0
for l in lines:
    l = l[:len(lines[0])-1]
    longest = 0
    second = 0
    c = 0
    while (c < len(l)):
        if int(l[c]) > longest and c != len(l)-1:
            longest = int(l[c])
            second = int(l[c+1])
        elif int(l[c]) > second:
            second = int(l[c])
        c += 1
    total += longest*10 + second

print(total)

