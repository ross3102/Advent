repl = []
mol = ""

with open("in.txt", "r") as file:
    line = file.readline()
    while line != "\n":
        line = line.strip().split()
        repl.append((line[0], line[2]))
        line = file.readline()
    mol = file.readline().strip()

mols = set()

for r in repl:
    frm = r[0]
    to = r[1]
    ln = len(frm)
    for i in range(len(mol)):
        if mol[i:i+ln] == frm:
            mols.add(mol[:i] + to + mol[i+ln:])

print(len(mols))