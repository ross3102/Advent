from os import path
file = open(path.dirname(__file__) + "/i", "r")

def solve():
    ans = 1
    times = list(map(int, file.readline().strip().split()[1:]))
    records = list(map(int, file.readline().strip().split()[1:]))
    for i in range(len(times)):
        t = times[i]
        r = records[i]

        ways = 0

        for i in range(t):
            dist = (t-i) * i
            if dist > r:
                ways += 1
        ans *= ways

    return ans

ans = solve()
print(ans)

file.close()