def getNeighbors(row, col, grid):
    n = []
    if row > 0:
        n.append(grid[row-1][col])
    if row < len(grid) - 1:
        n.append(grid[row+1][col])
    if col > 0:
        n.append(grid[row][col-1])
    if col < len(grid[row]) - 1:
        n.append(grid[row][col+1])
    return n


with open("in.txt", "r") as file:
    total = 0

    grid = [line.strip() for line in file]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            cur = int(grid[row][col])
            if all(cur < int(n) for n in getNeighbors(row, col, grid)):
                total += cur + 1
    print(total)
