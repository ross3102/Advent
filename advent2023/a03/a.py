from os import path
file = open(path.dirname(__file__) + "/i", "r")

def is_symbol(lines, i, j):
    if 0 <= i < len(lines) and 0 <= j < len(lines[i]):
        c = lines[i][j]
        return not c.isnumeric() and c != "."
    return False

def solve():
    ans = 0
    lines = []

    for line in file:
        line = line.strip()
        lines.append(line)
    for i in range(len(lines)):
        j = 0
        while j < len(lines[i]):
            c = lines[i][j]
            if c.isnumeric():
                touching = is_symbol(lines, i-1, j-1) or is_symbol(lines, i, j-1) or is_symbol(lines, i+1, j-1)
                val = 0
                while c.isnumeric():
                    touching = touching or is_symbol(lines, i-1, j) or is_symbol(lines, i+1, j)
                    val *= 10
                    val += int(c)
                    j += 1
                    if j >= len(lines[i]):
                        break
                    c = lines[i][j]
                touching = touching or is_symbol(lines, i-1, j) or is_symbol(lines, i, j) or is_symbol(lines, i+1, j)
                if touching:
                    print(val)
                    ans += val
            j += 1

    return ans

ans = solve()
print(ans)

file.close()