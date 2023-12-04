from os import path
file = open(path.dirname(__file__) + "/i", "r")

def solve():
    ms = []
    for line in file:
        line = line.strip()
        a, b = [list(map(int, x.split())) for x in line.split(": ")[1].split(" | ")]
        matches = 0
        for x in b:
            if x in a:
                matches += 1
        ms.append(matches)

    totals = [1] * len(ms)
    for i in range(len(ms)-1, -1, -1):
        m = ms[i]
        for j in range(i+1, min(len(ms), i+1+m)):
            totals[i] += totals[j]
    return sum(totals)

ans = solve()
print(ans)

file.close()