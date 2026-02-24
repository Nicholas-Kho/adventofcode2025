with open("day1.txt") as f:
    lines = f.readlines()


dial:int = 50
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
        num = code.split(array[0])[1]
        dial = turnDial(dial, int(num))
    elif array[0] == 'L':
        num = code.split(array[0])[1]
        dial = turnDial(dial, -int(num))
    else:
        print(array[0])
        raise Exception("Neither R or L")
    if (dial == 0):
        pointing += 1

print(dial)
print(pointing)

