def getRating(lines, isOxy):
    valid = [i for i in range(len(lines))]

    for i in range(len(lines[0])):
        withOne = []
        withoutOne = []
        zeros = 0
        ones = 0
        for lineNum in valid:
            line = lines[lineNum]
            if line[i] == "1":
                ones += 1
                withOne.append(lineNum)
            else:
                zeros += 1
                withoutOne.append(lineNum)
        if isOxy:
            if ones >= zeros:
                valid = withOne
            else:
                valid = withoutOne
        else:
            if ones < zeros:
                valid = withOne
            else:
                valid = withoutOne
        if len(valid) == 1:
            return int(lines[valid[0]], 2)


with open("in.txt", "r") as file:
    lines = [line.strip() for line in file]

    ox = getRating(lines, True)
    co2 = getRating(lines, False)

    print(ox * co2)
