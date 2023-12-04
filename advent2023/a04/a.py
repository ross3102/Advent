from os import path
file = open(path.dirname(__file__) + "/i", "r")

def solve():
    ans = 0
    for line in file:
        line = line.strip()
        a, b = [list(map(int, x.split())) for x in line.split(": ")[1].split(" | ")]
        points = 0
        for x in b:
            if x in a:
                if points == 0:
                    points = 1
                else:
                    points *= 2
        ans += points

    return ans

ans = solve()
print(ans)

file.close()