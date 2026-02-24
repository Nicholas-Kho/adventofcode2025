with open("day2.txt") as f:
    lines = f.read()

total = 0
for l in lines.split(","):
    left = l.split("-")[0]
    right = l.split("-")[1]
    for x in range(int(right)-int(left)+1):
        i = x+int(left)
        length = len(str(i))
        for y in range(1, int(length/2)+1):
            if (all(str(i)[:y] == str(i)[inc:y+inc] for inc in range(y, int(length), y))):
                total += i
                break

print(total)