from os import path
file = open(path.dirname(__file__) + "/i", "r")

def is_gear(lines, i, j):
    if 0 <= i < len(lines) and 0 <= j < len(lines[i]):
        c = lines[i][j]
        return c == "*"
    return False

def a_if_g(touching, lines, i, j):
    if is_gear(lines, i, j):
        touching.append((i, j))

def solve():
    ans = 0
    lines = []

    gears = {}

    for line in file:
        line = line.strip()
        lines.append(line)
    for i in range(len(lines)):
        j = 0
        while j < len(lines[i]):
            c = lines[i][j]
            touching = []
            if c.isnumeric():
                a_if_g(touching, lines, i-1, j-1)
                a_if_g(touching, lines, i, j-1)
                a_if_g(touching, lines, i+1, j-1)
                val = 0
                while c.isnumeric():
                    a_if_g(touching, lines, i-1, j)
                    a_if_g(touching, lines, i+1, j)
                    val *= 10
                    val += int(c)
                    j += 1
                    if j >= len(lines[i]):
                        break
                    c = lines[i][j]
                a_if_g(touching, lines, i-1, j)
                a_if_g(touching, lines, i, j)
                a_if_g(touching, lines, i+1, j)

                for g in touching:
                    gears[g] = gears.get(g, []) + [val]
            j += 1
    for g in gears.values():
        if len(g) == 2:
            ans += g[0] * g[1]
    return ans

ans = solve()
print(ans)

file.close()