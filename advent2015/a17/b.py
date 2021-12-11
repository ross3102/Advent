def combos(jars, i, amt):
  if amt < 0:
    return []
  if i == len(jars):
    return [[]] if amt == 0 else []

  withJar = [[i] + c for c in combos(jars, i+1, amt-jars[i])]
  withoutJar = combos(jars, i+1, amt)
  return withJar + withoutJar


sizes = []

with open("in.txt", "r") as file:
  for line in file:
    sizes.append(int(line.strip()))

cs = combos(sizes, 0, 150)

minSize = None
numCombos = 0
for c in cs:
  if minSize is None or len(c) < minSize:
    minSize = len(c)
    numCombos = 1
  elif len(c) == minSize:
    numCombos += 1

print(numCombos)