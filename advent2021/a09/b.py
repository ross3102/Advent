def getNeighbors(row, col, grid):
    n = []
    if row > 0:
        n.append([row-1, col])
    if row < len(grid) - 1:
        n.append([row+1, col])
    if col > 0:
        n.append([row, col-1])
    if col < len(grid[row]) - 1:
        n.append([row, col+1])
    return n


def findBasin(row, col, seen, grid):
    seen.append([row, col])
    for p in getNeighbors(row, col, grid):
        pr, pc = p
        if p not in seen and int(grid[pr][pc]) < 9 and int(grid[row][col]) < int(grid[pr][pc]):
            findBasin(pr, pc, seen, grid)


with open("in.txt", "r") as file:
    basins = []

    grid = [line.strip() for line in file]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            cur = int(grid[row][col])
            if all(cur < int(grid[p[0]][p[1]]) for p in getNeighbors(row, col, grid)):
                b = []
                findBasin(row, col, b, grid)
                basins.append(len(b))

    basins.sort()
    print(basins[-1] * basins[-2] * basins[-3])
