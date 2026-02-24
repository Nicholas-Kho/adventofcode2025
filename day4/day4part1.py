with open("day4.txt") as f:
    lines = f.readlines()

height = len(lines)
width = len(lines[0])-1

directions = [(-1, -1), (0, -1), (1, -1),(-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
print(sum(lines[x][y] == "@" and 4 > sum(x + h >= 0 and x + h < width and y + w >= 0 and y + w < height and lines[x + h][y + w] == "@" for h, w in directions) for x in range(height) for y in range(width)))