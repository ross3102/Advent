file = list(open("f.txt", "r"))

total = 0

i = 0

while i < len(file):
    offset = int(file[i])
    if offset < 3:
        file[i] = offset + 1
    else:
        file[i] = offset - 1
    i += offset
    total += 1

print(total)
