from os import path
file = open(path.dirname(__file__) + "/i", "r")

def solve():
    steps = 0
    p = file.readline().strip()
    mp = {}
    curs = []
    file.readline()
    line = file.readline()
    while line:
        line = line.strip()
        a, b = line.split(" = (")
        c, d = b.split(", ")
        mp[a] = (c, d[:-1])
        if a[-1] == "A":
            curs.append(a)
        line = file.readline()
    
    cycles = [-1] * len(curs)
    toFind = set(range(len(curs)))

    done = False
    while not done:
        for d in p:
            for i in range(len(curs)):
                cur = curs[i]
                if d == "L":
                    curs[i] = mp[cur][0]
                else:
                    curs[i] = mp[cur][1]
            steps += 1
        for i in range(len(curs)):
            cur = curs[i]
            if cur[-1] == "Z":
                cycles[i] = steps // len(p)
                toFind.remove(i)
                if len(toFind) == 0:
                    done = True

    # lcm(cycles) * len(p)

ans = solve()
print(ans)

file.close()