repl = []
goal = ""

with open("in.txt", "r") as file:
  line = file.readline()
  while line != "\n":
    line = line.strip().split()
    repl.append((line[0], line[2]))
    line = file.readline()
  goal = file.readline().strip()

def main():
  mols = set([goal])
  steps = 1
  while "e" not in mols:
    newmols = set()
    for mol in mols:
      for r in repl:
        frm = r[1]
        to = r[0]
        ln = len(frm)
        if to == "e":
          if mol == frm:
            return steps
          else:
            continue
        for i in range(len(mol)):
          if mol[i:i+ln] == frm:
            newmols.add(mol[:i] + to + mol[i+ln:])
    mols = newmols
    steps += 1
    print(len(mols), min(len(m) for m in mols), max(len(m) for m in mols))
    if len(mols) == 0:
      print("uhoh")
      return -1

print(main())
