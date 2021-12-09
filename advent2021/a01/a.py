with open("in.py", "r") as file:
    total = 0

    prev = None
    for line in file:
        i = int(line)
        if prev is not None and i > prev:
            total += 1
        prev = i
    print(total)
