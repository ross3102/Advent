file = open("i", "r")

def solve():
    target = 2000000
    occupied = set()
    for line in file:
        line = line.strip()
        line = line.split("x=")
        sx = int(line[1].split(", y=")[0])
        sy = int(line[1].split(", y=")[1].split(":")[0])

        bx = int(line[2].split(", y=")[0])
        by = int(line[2].split(", y=")[1].split(":")[0])

        dist = abs(sx - bx) + abs(sy - by)
        diff = abs(sy - target)
        armlen = dist - diff
        if armlen > 0:
            for i in range(sx - armlen, sx + armlen + 1):
                if (i, target) == (bx, by):
                    continue
                occupied.add(i)
    return len(list(occupied))
        
ans = solve()
print(ans)

file.close()