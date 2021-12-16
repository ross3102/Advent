def get_neighbors(x, y, grid):
    n = []
    if x > 0:
        n.append((x-1, y))
    if x < len(grid[y]) - 1:
        n.append((x+1, y))
    if y > 0:
        n.append((x, y-1))
    if y < len(grid) - 1:
        n.append((x, y+1))
    return n


grid = []
with open("in.txt", "r") as file:
    for line in file:
        grid.append([int(i) for i in line.strip()])

frontier = {}

frontier[(0, 0)] = 0

visited = set()
visited.add((0, 0))

found = False
while not found:
    x, y = min(frontier, key=lambda x: frontier[x])
    oldval = frontier[(x, y)]
    del frontier[(x, y)]
    for nx, ny in get_neighbors(x, y, grid):
        if (nx, ny) not in visited:
            frontier[(nx, ny)] = oldval + grid[ny][nx]
            visited.add((nx, ny))
        if ny == len(grid) - 1 and nx == len(grid[ny]) - 1:
            found = True
            break

print(frontier[(len(grid[-1]) - 1, len(grid) - 1)])
