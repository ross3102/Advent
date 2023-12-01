from os import path
file = open(path.dirname(__file__) + "/i", "r")

def solve():
    ans = 0
    for line in file:
        line = line.strip()
        ints = []
        for c in line:
            try:
                ints.append(str(int(c)))
            except:
                pass
        ans += int(ints[0] + ints[-1])
    return ans

ans = solve()
print(ans)

file.close()