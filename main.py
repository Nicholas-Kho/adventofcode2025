
with open("input.txt", "r") as f: input = f.read()

cubes = {"red": 12,
         "green": 13,
         "blue": 14}

total = 0


for line in input.split("\n"):
    possible = True
    l = line.split(";")
    print(l)
    game = l.pop(0)
    l.insert(0, game.split(":")[1])
    for i in range(len(l)):

        print(l)
        for cube in (l[i].lstrip()).split(","):
            cube = cube.lstrip()
            num1 = cubes[cube.split(" ")[1]]
            num2 = int(cube.split(" ")[0])
            if (num2 > num1):
                possible = False
    if possible:
        print(l, " ",int((game.split(" ")[1].split(":")[0])))
        total += int((game.split(" ")[1].split(":")[0]))
print(total)
