file = open('f', 'r')
lights = {}
for x in range(1000):
    for y in range(1000):
        lights[(x, y)] = 0
for line in file:
    line = line.split()
    coord1 = line[-3].split(",")
    coord2 = line[-1].split(",")
    command = line[:-3]
    if command == ['turn', 'on']:
        for x in range(int(coord1[0]), int(coord2[0]) + 1):
            for y in range(int(coord1[1]), int(coord2[1]) + 1):
                lights[(x, y)] += 1
    elif command == ['turn', 'off']:
        for x in range(int(coord1[0]), int(coord2[0]) + 1):
            for y in range(int(coord1[1]), int(coord2[1]) + 1):
                lights[(x, y)] -= 1
                if lights[(x, y)] < 0:
                    lights[(x, y)] = 0
    else:
        for x in range(int(coord1[0]), int(coord2[0]) + 1):
            for y in range(int(coord1[1]), int(coord2[1]) + 1):
                lights[(x, y)] += 2
total = sum(list(lights.values()))
print(total)
