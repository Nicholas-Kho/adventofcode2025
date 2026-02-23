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
    if array[0] == 'R':
        amount = int(code.split(array[0])[1])
        num += int(amount)
        pointing += abs(math.floor(amount / 99))
        pointing += 1 if num != num % 100 and abs(math.floor(amount / 99)) else 0
        num = num % 100
    elif array[0] == 'L':
        amount = int(code.split(array[0])[1])
        num += -int(amount)
        pointing += abs(math.floor(amount / 99))
        pointing += 1 if num != num % 100 and abs(math.floor(amount / 99)) == 0 else 0
        num = num % 100
    else:
        print(array[0])
        raise Exception("Neither R or L")


print(num)
print(pointing)

