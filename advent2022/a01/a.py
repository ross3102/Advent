with open("i", "r") as file:
    mx = 0
    tot = 0
    for line in file:
        line = line.strip()
        if len(line) == 0:
            mx = max(mx, tot)
            tot = 0
        else:
            tot += int(line)
    print(mx)