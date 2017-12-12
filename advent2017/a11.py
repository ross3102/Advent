def steps(x, y):
    return x + (y - x/2)

def p1(file):
    x = 0
    y = 0
    directions = [i for i in file[0].split(",")]

    for d in directions:
        if d == "n":
            y += 1
        elif d == "ne":
            y += .5
            x += 1
        elif d == "nw":
            y += .5
            x -= 1
        elif d == "s":
            y -= 1
        elif d == "se":
            y -= .5
            x += 1
        elif d == "sw":
            y -= .5
            x -= 1
    return x, y

def p2(file):
    maxX = 0
    maxY = 0
    x = 0
    y = 0
    directions = [i for i in file[0].split(",")]

    for d in directions:
        if d == "n":
            y += 1
        elif d == "ne":
            y += .5
            x += 1
        elif d == "nw":
            y += .5
            x -= 1
        elif d == "s":
            y -= 1
        elif d == "se":
            y -= .5
            x += 1
        elif d == "sw":
            y -= .5
            x -= 1
        if steps(abs(x), abs(y)) > steps(abs(maxX), abs(maxY)):
            maxX = x
            maxY = y
    return steps(abs(maxX), abs(maxY))


file = list(open("f.txt", "r"))
print(p2(file))
#