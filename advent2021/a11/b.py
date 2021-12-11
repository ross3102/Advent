grid = []
with open("in.txt", "r") as file:
    for line in file:
        grid.append([int(i) for i in line.strip()])

step = 1
while True:
    flashes = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            grid[row][col] += 1

    flashed = set()
    changed = True
    while changed:
        changed = False
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] > 9 and (row, col) not in flashed:
                    flashed.add((row, col))
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if 0 <= row + i < len(grid) and 0 <= col + j < len(grid[row]):
                                grid[row+i][col+j] += 1
                                changed = True

    for pair in flashed:
        grid[pair[0]][pair[1]] = 0
        flashes += 1
    if flashes == len(grid) * len(grid[0]):
      break
    step += 1

print(step)
