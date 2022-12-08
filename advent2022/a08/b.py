file = open("i", "r")

def solve():
    grid = []
    for line in file:
        line = line.strip()
        grid.append([int(i) for i in line])

    hi = 0

    for trow in range(len(grid)):
        for tcol in range(len(grid[trow])):
            cur = grid[trow][tcol]
            up = 0
            for row in range(trow-1, -1, -1):
                up += 1
                if grid[row][tcol] >= cur:
                    break
                
            down = 0
            for row in range(trow+1, len(grid)):
                down += 1
                if grid[row][tcol] >= cur:
                    break
            left = 0
            for col in range(tcol-1, -1, -1):
                left += 1
                if grid[trow][col] >= cur:
                    break
                
            right = 0
            for col in range(tcol+1, len(grid[trow])):
                right += 1
                if grid[trow][col] >= cur:
                    break
                
            score = up * down * left * right
            hi = max(hi, score)
    
    return hi

ans = solve()
print(ans)

file.close()