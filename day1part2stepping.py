with open("day1.txt") as f:
    lines = f.readlines()

cog = 50
pointing = 0
for l in lines:
    direction = 1 if list(l)[0] == 'R' else -1
    amount = int(l[1:])
    #print(direction, amount, l, cog)
    for i in range(amount):
        cog += direction
        cog = cog % 100
        if (cog == 0):
            pointing += 1


        #print(cog, pointing)

print(pointing)