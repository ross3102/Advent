def findPaths(cur, seen, paths, twice=False):
    if cur == 'end':
        return [[cur]]
    if cur != cur.upper():
        seen = seen + [cur]

    ans = []
    for next in paths[cur]:
        if next in seen:
            if not twice and next != 'start':
                for p in findPaths(next, seen, paths, True):
                    ans.append([cur] + p)
        else:
            for p in findPaths(next, seen, paths, twice):
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
