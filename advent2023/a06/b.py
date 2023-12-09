from os import path
file = open(path.dirname(__file__) + "/i", "r")

def solve():
    ans = 1
    t = int("".join(file.readline().strip().split()[1:]))
    r = int("".join(file.readline().strip().split()[1:]))

    ways = 0

    for i in range(t):
        dist = (t-i) * i
        if dist > r:
            ways += 1

    return ways

ans = solve()
print(ans)

file.close()