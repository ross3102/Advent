file = open("i", "r")

def solve():
    visible = set()
    grid = []
    for line in file:
        line = line.strip()
        grid.append([int(i) for i in line])
    
    for row in range(len(grid)):
        highest = -1
        for col in range(len(grid[row])):
            if grid[row][col] > highest:
                highest = grid[row][col]
                visible.add((row, col))
        highest = -1
        for col in range(len(grid[row])-1, -1, -1):
            if grid[row][col] > highest:
                highest = grid[row][col]
                visible.add((row, col))
    for col in range(len(grid[0])):
        highest = -1
        for row in range(len(grid)):
            if grid[row][col] > highest:
                highest = grid[row][col]
                visible.add((row, col))
        highest = -1
        for row in range(len(grid)-1, -1, -1):
            if grid[row][col] > highest:
                highest = grid[row][col]
                visible.add((row, col))
        
    return len(list(visible))

ans = solve()
print(ans)

file.close()