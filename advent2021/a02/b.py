with open("in.txt", "r") as file:
    pos = 0
    depth = 0
    aim = 0

    for line in file:
        d, n = line.split()
        n = int(n)
        if d == "down":
            aim += n
        elif d == "up":
            aim -= n
        else:
            pos += n
            depth += aim * n

    print(pos * depth)
