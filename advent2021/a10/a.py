matching = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}

pts = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

with open("in.txt", "r") as file:
    total = 0
    for line in file:
        line = line.strip()
        stack = []
        for c in line:
            if c in "([{<":
                stack.append(c)
            else:
                if len(stack) == 0 or stack[-1] != matching[c]:
                    total += pts[c]
                    break
                else:
                    del stack[-1]
    print(total)
