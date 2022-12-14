file = open("i", "r")

def is_occupied(occupied, bottom, x, y):
    return (x, y) in occupied or y >= bottom

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
    bottom += 2
    tot = 0
    sand = (500, 0)
    while (500, 0) not in occupied:
        if not is_occupied(occupied, bottom, sand[0], sand[1]+1):
            sand = (sand[0], sand[1]+1)
        elif not is_occupied(occupied, bottom, sand[0]-1, sand[1]+1):
            sand = (sand[0]-1, sand[1]+1)
        elif not is_occupied(occupied, bottom, sand[0]+1, sand[1]+1):
            sand = (sand[0]+1, sand[1]+1)
        else:
            occupied.add(sand)
            tot += 1
            sand = (500, 0)
    return tot


ans = solve()
print(ans)

file.close()
