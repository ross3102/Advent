def add_counts(d1, d2):
  counts = {}
  for k in d1:
    counts[k] = d1[k]
  for k in d2:
    counts[k] = d1.get(k, 0) + d2[k]
  return counts

def letter_counts(l1, l2, steps, conv, memo):
  if (l1, l2, steps) in memo:
    return memo[(l1, l2, steps)]

  if steps == 0:
    counts = add_counts({l1: 1}, {l2: 1})
    memo[(l1, l2, steps)] = counts
    return counts

  mid = conv[l1 + l2]
  counts = add_counts(
    letter_counts(l1, mid, steps - 1, conv, memo),
    letter_counts(mid, l2, steps - 1, conv, memo))
  counts[mid] -= 1
  memo[(l1, l2, steps)] = counts
  return counts

conv = {}
init = ""

with open("in.txt", "r") as file:
  init = file.readline().strip()
  file.readline()
  line = file.readline()
  while line:
    frm, to = line.strip().split(" -> ")
    conv[frm] = to
    line = file.readline()

memo = {}
counts = letter_counts(init[0], init[1], 40, conv, memo)
for i in range(1, len(init) - 1):
  counts = add_counts(counts, letter_counts(init[i], init[i+1], 40, conv, memo))
  counts[init[i]] -= 1 # Remove overlapping letter

print(max(counts.values()) - min(counts.values()))