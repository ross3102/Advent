def findPath(curLoc, seen, total, paths, numLocs):
    if len(seen) == numLocs:
        return total
    acc = paths.get(curLoc, {})
    longest = -1
    for nLoc, amt in acc.items():
        if nLoc not in seen:
            ln = findPath(nLoc, seen + [nLoc], total + amt, paths, numLocs)
            if ln != -1 and (longest == -1 or ln > longest):
                longest = ln
    return longest


paths = {}
locs = set()

with open("in.txt", "r") as file:
    for line in file:
        line = line.split(" = ")
        places = line[0]
        dist = int(line[1])
        frm, to = places.split(" to ")
        t = paths.get(frm, {})
        t[to] = dist
        paths[frm] = t
        t = paths.get(to, {})
        t[frm] = dist
        paths[to] = t
        locs.add(frm)
        locs.add(to)

    longest = -1
    for nLoc in locs:
        ln = findPath(nLoc, [nLoc], 0, paths, len(locs))
        if ln != -1 and (longest == -1 or ln > longest):
            longest = ln
    print(longest)
