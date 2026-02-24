with open("day4.txt") as f:
    lines = f.readlines()

height = len(lines)
width = len(lines[0])-1

directions = [(-1, -1), (0, -1), (1, -1),(-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

clear = True
total = 0

while clear:
    toClear = []
    for x in range(width):
        for y in range(height):
            if lines[x][y] == '@' and 4 > sum(x + h >= 0 and x + h < width and y + w >= 0 and y + w < height and lines[x+h][y+w] == '@' for h, w in directions):
                total += 1
                toClear.append((x, y))
    if len(toClear) == 0:
        clear = False
    else:
        for coord in toClear:
            lines[coord[0]] = lines[coord[0]][:coord[1]] + '.' + lines[coord[0]][coord[1]+1:]

print(total)