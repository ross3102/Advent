file = open("i", "r")

def solve():
    line = file.readline().strip()
    for i in range(len(line)):
        s = list(set([line[x] for x in range(i, i+14)]))
        if len(s) == 14:
            return i+14
        

ans = solve()
print(ans)

file.close()