file = open("advent2015/f", "r")

total = 0

for line in file:
    line = line.strip()
    originalLength = len(line)
    newLength = len(line) + 2


    newLength += 2 * line.count("\\\\")
    line = line.replace("\\\\", "")
    newLength += 1 * line.count("\\x")
    newLength += 2 * line.count("\\\"")
    line = line.replace("\\\"", "")
    newLength += 1 * line.count("\"")
    print(originalLength)
    print(newLength)

    total += (newLength - originalLength)
print(total)