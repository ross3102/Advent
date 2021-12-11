matching = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}

pts = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}

with open("in.txt", "r") as file:
    totals = []
    for line in file:
        curtot = 0
        line = line.strip()
        mismatched = False
        stack = []
        for c in line:
            if c in "([{<":
                stack.append(c)
            else:
                if len(stack) == 0 or stack[-1] != matching[c]:
                    mismatched = True
                    break
                else:
                    del stack[-1]
        if mismatched:
            continue
        for c in stack[::-1]:
            curtot *= 5
            curtot += pts[c]
        totals.append(curtot)
    totals.sort()
    print(totals[len(totals)//2])
