def go(i, points):
    newpoints = []
    for point in points:
        x = point[0]
        y = point[1]
        if x > 0:
            add(x - 1, y, newpoints)
        if y > 0:
            add(x, y - 1, newpoints)
        add(x + 1, y, newpoints)
        add(x, y + 1, newpoints)
    points = newpoints
    i = i + 1
    if i == 50:
        print(len(seen))
    else:
        go(i, points)

def add(x, y, newpoints):
    if (x, y) not in seen and not iswall((x, y)):
        seen.append((x, y))
        newpoints.append((x, y))

def iswall(point):
    x = point[0]
    y = point[1]
    return str(bin(x*x + 3*x + 2*x*y + y + y*y + 1350))[2:].count('1') % 2 == 1

points = [(1,1)]
seen = [(1,1)]

i = go(0, points)
