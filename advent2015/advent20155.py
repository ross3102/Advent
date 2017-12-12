file = open('f', 'r')
total = 0
for line in file:
    points = [False, False]
    for x in range(len(line) - 1):
        new = list(line)
        search = line[x:x+2]
        del new[x]
        new[x] = "googgooggoog"
        for y in range(len(new) - 1):
            if "".join(new[y:y+2]) == search:
                points[0] = True
    for x in range(len(line) - 2):
        if line[x] == line[x+2]:
            points[1] = True
    if points == [True, True]:
        total += 1
        print(line)
print(total)
