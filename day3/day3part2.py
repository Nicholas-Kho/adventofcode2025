with open("day3.txt") as f:
    lines = f.readlines()

total = 0
for l in lines:
    l = l[:len(lines[0])-1]
    #print(l)
    sub = 0
    c = 0
    digits = ""
    while c < len(l):
        if len(digits) >= 12:
            for i in range(0, 12):
                #print(i)
                push = int(digits[:i] + digits[i+1:])*10 + int(l[c])
                #print(push, ": ", push > int(digits), " - ", digits, " = ", l[c])
                if push > int(digits):
                    digits = str(push)
                    sub = int(digits)
                    break
        else:
            sub = sub * 10 + int(l[c])
            digits += l[c]
        c += 1
    #print(sub)
    total += sub

print(total)