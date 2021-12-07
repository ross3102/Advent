with open("i07.txt", "r") as file:
    line = [int(i) for i in file.readline().split(",")]
    mintotal = -1
    for pos in range(min(line), max(line)):
        curtotal = 0
        for pos2 in line:
            curtotal += abs(pos2 - pos)
        if mintotal == -1 or curtotal < mintotal:
            mintotal = curtotal
    print(mintotal)
