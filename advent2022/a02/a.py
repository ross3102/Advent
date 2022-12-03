file = open("i", "r")

beats = {
    "A": "Z",
    "B": "X",
    "C": "Y",
    "X": "C",
    "Y": "A",
    "Z": "B"
}

def solve():
    metot = 0
    themtot = 0
    for line in file:
        a, x = line.strip().split()
        me = ord(x) - ord("X") + 1
        them = ord(a) - ord("A") + 1
        if beats[x] == a:
            me += 6
        elif beats[a] == x:
            them += 6
        elif me == them:
            me += 3
            them += 3
        metot += me
        themtot += them
    return metot

ans = solve()
print(ans)

file.close()