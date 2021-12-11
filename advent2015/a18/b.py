def appendIfExists(grid, row, col, lst):
    if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[row]):
        lst.append(grid[row][col])


def numNeighborsOn(grid, row, col):
    n = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            appendIfExists(grid, row + i, col + j, n)
    return len([i for i in n if i])


grid = []

with open("in.txt", "r") as file:
    for line in file:
        grid.append([c == "#" for c in line.strip()])

for step in range(100):
    newGrid = []
    for row in range(len(grid)):
        newRow = []
        for col in range(len(grid[row])):
            if row in (0, len(grid)-1) and col in (0, len(grid[row])-1):
                newRow.append(True)
                continue

            n = numNeighborsOn(grid, row, col)
            if grid[row][col] and n in (2, 3):
                newRow.append(True)
            elif not grid[row][col] and n == 3:
                newRow.append(True)
            else:
                newRow.append(False)
        newGrid.append(newRow)
    grid = newGrid

print(sum([row.count(True) for row in grid]))
