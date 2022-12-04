file = open("i", "r")

def solve():
    ans = 0
    for line in file:
        a, b = line.strip().split(",")
        a1, a2 = map(int, a.split("-"))
        b1, b2 = map(int, b.split("-"))
        if not (a2 < b1 or b2 < a1):
            ans += 1
    return ans

ans = solve()
print(ans)

file.close()