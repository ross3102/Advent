file = open("i", "r")

class Scanner:
    def __init__(self, x, y, dist):
        self.x = x
        self.y = y
        self.dist = dist

    def contains(self, x, y):
        return abs(self.x - x) + abs(self.y - y) <= self.dist

def solve():
    mx = 4000000
    scanners = []
    for line in file:
        line = line.strip()
        line = line.split("x=")
        sx = int(line[1].split(", y=")[0])
        sy = int(line[1].split(", y=")[1].split(":")[0])
        bx = int(line[2].split(", y=")[0])
        by = int(line[2].split(", y=")[1].split(":")[0])

        dist = abs(sx - bx) + abs(sy - by)
        scanners.append(Scanner(sx, sy, dist))

    for s1 in scanners:
        dist = s1.dist
        sx = s1.x
        sy = s1.y
        for i in range(dist+2):
            x = sx+i
            y = sy+dist+1-i
            if 0 <= x <= mx and 0 <= y <= mx:
                if not any(s.contains(x, y) for s in scanners):
                    return 4000000 * x + y
            x = sx+i
            y = sy-dist-1+i
            if 0 <= x <= mx and 0 <= y <= mx:
                if not any(s.contains(x, y) for s in scanners):
                    return 4000000 * x + y
            x = sx-i
            y = sy+dist+1-i
            if 0 <= x <= mx and 0 <= y <= mx:
                if not any(s.contains(x, y) for s in scanners):
                    return 4000000 * x + y
            x = sx-i
            y = sy-dist-1+i
            if 0 <= x <= mx and 0 <= y <= mx:
                if not any(s.contains(x, y) for s in scanners):
                    return 4000000 * x + y
        
ans = solve()
print(ans)

file.close()