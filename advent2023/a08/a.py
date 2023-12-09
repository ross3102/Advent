from os import path
file = open(path.dirname(__file__) + "/i", "r")

def solve():
    ans = 0
    p = file.readline().strip()
    mp = {}
    file.readline()
    line = file.readline()
    while line:
        line = line.strip()
        a, b = line.split(" = (")
        c, d = b.split(", ")
        mp[a] = (c, d[:-1])
        line = file.readline()
    
    cur = "AAA"

    while True:
        for d in p:
            if cur == "ZZZ":
                return ans
            if d == "L":
                cur = mp[cur][0]
            else:
                cur = mp[cur][1]
            ans += 1

ans = solve()
print(ans)

file.close()