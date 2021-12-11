# Number of ways to use jars[i:] to make amt
def numCombos(jars, i, amt):
    if amt < 0:
        return 0
    if i == len(jars):
        return 1 if amt == 0 else 0

    return numCombos(jars, i+1, amt-jars[i]) + numCombos(jars, i+1, amt)

sizes = []

with open("in.txt", "r") as file:
    for line in file:
        sizes.append(int(line.strip()))

print(numCombos(sizes, 0, 150))