from os import path
file = open(path.dirname(__file__) + "/i", "r")

amounts = {
    "red": 12,
    "green": 13,
    "blue": 14    
}

def solve():
    ans = 0
    for line in file:
        line = line.strip()
        id = int(line.split(": ")[0].split()[1])
        stuff = line.split(": ")[1]
        rounds = stuff.split("; ")
        good = True
        for r in rounds:
            things = r.split(", ")
            for t in things:
                n, c = t.split(" ")
                if int(n) > amounts[c]:
                    good = False

        if good:
            ans += id
    return ans

ans = solve()

print(ans)
