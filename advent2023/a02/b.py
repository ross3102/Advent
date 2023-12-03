from os import path
file = open(path.dirname(__file__) + "/i", "r")

def solve():
    ans = 0
    for line in file:
        line = line.strip()
        stuff = line.split(": ")[1]
        rounds = stuff.split("; ")
        maxes = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for r in rounds:
            things = r.split(", ")
            for t in things:
                n, c = t.split(" ")
                maxes[c] = max(maxes[c], int(n))
        ans += maxes["red"] * maxes["green"] * maxes["blue"]
    return ans

ans = solve()
print(ans)
