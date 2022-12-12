file = open("i", "r")


def canMove(grid, f, t):
    tcol, trow = t
    fcol, frow = f
    if 0 <= trow < len(grid) and 0 <= tcol < len(grid[trow]):
        return grid[trow][tcol] <= grid[frow][fcol] + 1
    return False


def solve():
    grid = []
    locs = []
    end = None
    row = 0
    for line in file:
        line = line.strip()
        gridrow = []
        for col in range(len(line)):
            c = line[col]
            if c == "S" or c == "a":
                gridrow.append(0)
                locs.append((col, row))
            elif c == "E":
                gridrow.append(25)
                end = (col, row)
            else:
                gridrow.append(ord(c) - ord('a'))
        grid.append(gridrow)
        row += 1
    seen = set([locs[0]])
    steps = 0
    while True:
        newlocs = []
        for loc in locs:
            lcol, lrow = loc
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                to = (lcol + dx, lrow + dy)
                if to not in seen and canMove(grid, loc, to):
                    newlocs.append(to)
                    seen.add(to)
                    if to == end:
                        return steps + 1
        locs = newlocs
        steps += 1


ans = solve()
print(ans)

file.close()
