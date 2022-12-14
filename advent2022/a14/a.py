file = open("i", "r")

def solve():
    occupied = set()
    bottom = 0
    for line in file:
        line = line.strip()
        line = [list(map(int, s.split(","))) for s in line.split(" -> ")]
        for i in range(len(line) - 1):
            p1 = line[i]
            p2 = line[i+1]
            if p1[0] == p2[0]:
                x = p1[0]
                miny = min(p1[1], p2[1])
                maxy = max(p1[1], p2[1])
                for y in range(miny, maxy+1):
                    occupied.add((x, y))
                    if y > bottom:
                        bottom = y
            else:
                y = p1[1]
                minx = min(p1[0], p2[0])
                maxx = max(p1[0], p2[0])
                for x in range(minx, maxx+1):
                    occupied.add((x, y))
                if y > bottom:
                    bottom = y

    tot = 0
    sand = (500, 0)
    while sand[1] < bottom:
        if (sand[0], sand[1]+1) not in occupied:
            sand = (sand[0], sand[1]+1)
        elif (sand[0]-1, sand[1]+1) not in occupied:
            sand = (sand[0]-1, sand[1]+1)
        elif (sand[0]+1, sand[1]+1) not in occupied:
            sand = (sand[0]+1, sand[1]+1)
        else:
            occupied.add(sand)
            tot += 1
            sand = (500, 0)
    return tot

ans = solve()
print(ans)

file.close()