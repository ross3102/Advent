file = open("i", "r")

beats = {
    "A": "C",
    "B": "A",
    "C": "B",
}

loses = {
    "A": "B",
    "B": "C",
    "C": "A",
}

def val(c):
    return ord(c) - ord("A") + 1

def solve():
    me = 0
    for line in file:
        a, x = line.strip().split()
        if x == "Z":
            me += val(loses[a]) + 6
        elif x == "Y":
            me += val(a) + 3
        else:
            me += val(beats[a])
    return me

ans = solve()
print(ans)

file.close()