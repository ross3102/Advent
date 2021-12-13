def foldX(dots, mn):
    newDots = set()
    for d in dots:
        newX = d[0]
        newY = d[1]
        if d[0] > mn:
            newX = 2*mn - newX
        newDots.add((newX, newY))
    return newDots


def foldY(dots, mn):
    newDots = set()
    for d in dots:
        newX = d[0]
        newY = d[1]
        if d[1] > mn:
            newY = 2*mn - newY
        newDots.add((newX, newY))
    return newDots


def doFold(dots, fold):
    if fold[0] == "x":
        return foldX(dots, fold[1])
    else:
        return foldY(dots, fold[1])


dots = set()
folds = []

with open("in.txt", "r") as file:
    line = file.readline()
    while line != "\n":
        x, y = map(int, line.strip().split(","))
        dots.add((x, y))
        line = file.readline()
    line = file.readline()
    while line:
        axis, num = line.strip().split(" ")[2].split("=")
        folds.append((axis, int(num)))
        line = file.readline()

for f in folds:
    dots = doFold(dots, f)

width = max(d[0] for d in dots) + 1
height = max(d[1] for d in dots) + 1

for row in range(height):
    for col in range(width):
        if (col, row) in dots:
            print("#", end="")
        else:
            print(" ", end="")
    print()
