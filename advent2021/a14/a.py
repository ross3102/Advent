conv = {}
temp = ""
unq = set()

with open("in.txt", "r") as file:
    temp = file.readline().strip()
    file.readline()
    line = file.readline()
    while line:
        frm, to = line.strip().split(" -> ")
        unq.add(frm[0])
        unq.add(frm[1])
        unq.add(to)

        conv[frm] = to
        line = file.readline()

for step in range(10):
    newtemp = temp[0]
    for i in range(len(temp) - 1):
        cur = temp[i]
        nxt = temp[i+1]
        newtemp += conv[cur + nxt] + nxt
    temp = newtemp

uql = list(unq)
uql.sort(key=lambda x: temp.count(x))
print(temp.count(uql[-1]) - temp.count(uql[0]))
