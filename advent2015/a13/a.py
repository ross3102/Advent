def arrangements(l, exclude):
    if len(exclude) == len(l):
        return [[]]
    ans = []
    for p in l:
        if p not in exclude:
            new = arrangements(l, exclude + [p])
            for a in new:
                ans.append([p] + a)
    return ans


deltas = {}

with open("in.txt", "r") as file:
    for line in file:
        line = line.strip().split()
        p1 = line[0]
        sign = 1 if line[2] == "gain" else -1
        amount = sign * int(line[3])
        p2 = line[-1][:-1]

        tmp = deltas.get(p1, {})
        tmp[p2] = amount
        deltas[p1] = tmp
    arrs = arrangements(deltas.keys(), [])

    opt = None
    for a in arrs:
        delta = 0
        for i in range(len(a)):
            previ = (i-1+len(a)) % len(a)
            nexti = (i + 1) % len(a)
            delta += deltas[a[i]][a[previ]] + deltas[a[i]][a[nexti]]
        if opt is None or delta > opt:
            opt = delta

    print(opt)
