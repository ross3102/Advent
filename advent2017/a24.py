# Warning: Takes several hours to run

def p1and2(file):
    components = []
    for line in file:
        line = line.strip().split("/")
        components.append([int(line[0]),int(line[1])])
        components.append([int(line[1]),int(line[0])])

    bridges = []

    for c in components:
        if c[0] == 0:
            bridges.append([c])

    done = False
    while not done:
        strengths = []
        lengths = []
        for bNum in range(len(bridges)):
            strengths.append(sum([sum(c) for c in bridges[bNum]]))
            lengths.append(len(bridges[bNum]))
        maxLen = max(lengths)
        print(maxLen)
        done = True

        upTo = len(bridges)
        bNum = lengths.index(maxLen)
        while bNum < upTo:
            b = bridges[bNum]
            if len(b) == maxLen:
                for c in components:
                    if c[0] == b[-1][-1] and c not in b and c[::-1] not in b:
                        newb = [i for i in b] + [c]
                        if newb not in bridges:
                            bridges.append(newb)
                            done = False
            bNum += 1
    strengths = []
    for bNum in range(len(bridges)):
        if len(bridges[bNum]) == maxLen:  # Condition only for part 2
            strengths.append(sum([sum(c) for c in bridges[bNum]]))
    return max(strengths)


file = list(open("f.txt", "r"))
print(p1and2(file))