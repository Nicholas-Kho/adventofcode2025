with open("day2.txt") as f:
    lines = f.read()



total = 0
for l in lines.split(","):
    left = l.split("-")[0]
    right = l.split("-")[1]
    for x in range(int(right)-int(left)+1):
        i = x+int(left)
        length = len(str(i))
        if len(str(i)) % 2 == 0:
            if (str(i)[:int(length/2)] == str(i)[int(length/2):]):
                total += i


print(total)