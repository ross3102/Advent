def findPaths(cur, seen, paths):
    if cur == 'end':
        return [[cur]]
    if cur != cur.upper():
        seen = seen + [cur]

    ans = []
    for next in paths[cur]:
        if next in seen:
            continue
        for p in findPaths(next, seen, paths):
            ans.append([cur] + p)
    return ans


paths = {}

with open("in.txt", "r") as file:
    for line in file:
        start, end = line.strip().split("-")
        ends = paths.get(start, set())
        ends.add(end)
        paths[start] = ends
        starts = paths.get(end, set())
        starts.add(start)
        paths[end] = starts

print(len(findPaths('start', [], paths)))
