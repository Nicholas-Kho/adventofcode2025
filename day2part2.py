with open("day2.txt") as f:
    lines = f.read()

total = 0
for l in lines.split(","):
    left = l.split("-")[0]
    right = l.split("-")[1]
    for x in range(int(right)-int(left)+1):
        i = x+int(left)
        #print(i)
        length = len(str(i))
        for y in range(1, int(length/2)+1):
            #print(i, " = ", str(i)[:y], " to ", str(i)[y:y*2], ": ", (all(str(i)[:y] == str(i)[y:y+inc] for inc in range(y, length+1, y))))
            if (all(str(i)[:y] == str(i)[y:y+inc] for inc in range(y, length+1, y))):
                total += i
                break

print(total)

#length=2
#y=1
#print((all(str(11)[:y] == str(11)[y:inc] for inc in range(y, length+1, y))))
#for inc in range(y, length, y):
#    print("iteration")
#    print(str(11)[:y])
#    print(str(11)[y:y+inc])
#    print(str(11)[:y] == str(11)[y:y+inc])