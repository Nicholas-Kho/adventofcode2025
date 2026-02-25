with open("day5.txt") as f:
    lines = f.read()

total = 0
range = lines.split("\n\n")[0].split("\n")
id = lines.split("\n\n")[1].split("\n")

for i in id:
    print(i)
    for r in range:
        if int(i) >= int(r.split("-")[0]) and int(i) <= int(r.split("-")[1]):
            total += 1
            break

print(total)
