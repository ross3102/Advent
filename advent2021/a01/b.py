with open("in.txt", "r") as file:
    total = 0

    prevs = []

    for i in range(3):
        line = file.readline()
        prevs.append(int(line))

    line = file.readline()
    while line:
        if int(line) > prevs[0]:
            total += 1
        del prevs[0]
        prevs.append(int(line))
        line = file.readline()
    print(total)
