with open("i", "r") as file:
    mx = []
    tot = 0
    for line in file:
        line = line.strip()
        if len(line) == 0:
            mx.append(tot)
            tot = 0
        else:
            tot += int(line)
    mx.sort()
    print(sum(mx[-3:]))