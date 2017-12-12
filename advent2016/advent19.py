file = open("f", "r")

nums = []

for line in file:
    line = line.split("-")
    start = int(line[0])
    end = int(line[1])
    nums.append((start, end))

for tup in nums:
    if tup[1] < 14975795:
        print(tup)

i = 14975793

total = 0

while i < 4294967295:
    done = True
    i += 1
    for tup in nums:
        if tup[0] <= i and tup[1] >= i:
            done = False
    if not done:
        continue
    total += 1
    print(total)
print(total)