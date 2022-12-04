file = open("i", "r")

def solve():
    ans = 0
    for line in file:
        a, b = line.strip().split(",")
        a1, a2 = map(int, a.split("-"))
        b1, b2 = map(int, b.split("-"))
        if a1 <= b1 and a2 >= b2 or b1 <= a1 and b2 >= a2:
            ans += 1
    return ans

ans = solve()
print(ans)

file.close()