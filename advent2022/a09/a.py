file = open("i", "r")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        self.x += other.x
        self.y += other.y

deltas = {
    "U": Point(0, 1),
    "D": Point(0, -1),
    "L": Point(-1, 0),
    "R": Point(1, 0)
}

def solve():
    visited = set([(0, 0)])
    h = Point(0, 0)
    t = Point(0, 0)
    for line in file:
        line = line.strip().split()
        c = line[0]
        n = int(line[1])
        for i in range(n):
            h.add(deltas[c])
            if h.x - t.x >= 2:
                t.x = h.x - 1
                if h.y > t.y:
                    t.y += 1
                elif h.y < t.y:
                    t.y -= 1
            if t.x - h.x >= 2:
                t.x = h.x + 1
                if h.y > t.y:
                    t.y += 1
                elif h.y < t.y:
                    t.y -= 1
            if h.y - t.y >= 2:
                t.y = h.y - 1
                if h.x > t.x:
                    t.x += 1
                elif h.x < t.x:
                    t.x -= 1
            if t.y - h.y >= 2:
                t.y = h.y + 1
                if h.x > t.x:
                    t.x += 1
                elif h.x < t.x:
                    t.x -= 1
            visited.add((t.x, t.y))
    return len(list(visited))

ans = solve()
print(ans)

file.close()