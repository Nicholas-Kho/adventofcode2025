import math

with open("day1.txt") as f:
    lines = f.readlines()


num:int = 50
pointing = 0

def turnDial(num, amount):
    num += int(amount)
    num = num % 100
    return num




for l in lines:
    code = l.split("\n")[0]
    array = list(code)
    print(array)

    start = num
    direction = 1 if array[0] == 'R' else -1
    amount = int(l[1:])
    num += direction * amount
    pointing += abs(math.floor(num/99))
    #pointing += 1 if (math.floor(num/100) == 0) and math.floor(start/100) == 0 else 0
    #pointing -= 1 if start == 0 and direction == -1 else 0
    num = num % 100
    # i think i suck at maths so i guve up and im doing it the easy way (stepping)


    print(num, ", ", pointing)


print(num)
print(pointing)