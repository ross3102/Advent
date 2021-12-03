dirs = {
    "down": [0, -1],
    "up": [0, 1],
    "forward": [1, 0]
}

with open("i02.txt", "r") as file:
    pos = 0
    depth = 0

    for line in file:
        d, n = line.split()
        n = int(n)
        pos += dirs[d][0] * n
        depth -= dirs[d][1] * n

    print(pos * depth)
