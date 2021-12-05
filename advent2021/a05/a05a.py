with open("i05.txt", "r") as file:
    pointCounts = {}
    total = 0
    for line in file:
        start, end = line.strip().split(" -> ")
        start = [int(i) for i in start.split(",")]
        end = [int(i) for i in end.split(",")]
        if start[0] == end[0]:
            counts = pointCounts.get(start[0], {})
            for i in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
                counts[i] = counts.get(i, 0) + 1
                if counts[i] == 2:
                    total += 1
            pointCounts[start[0]] = counts
        elif start[1] == end[1]:
            for i in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
                counts = pointCounts.get(i, {})
                counts[start[1]] = counts.get(start[1], 0) + 1
                if counts[start[1]] == 2:
                    total += 1
                pointCounts[i] = counts
    print(total)
