file = open("i", "r")

def solve():
    line = file.readline().strip()
    for i in range(len(line)):
        s = list(set([line[x] for x in range(i, i+4)]))
        if len(s) == 4:
            return i+4

ans = solve()
print(ans)

file.close()