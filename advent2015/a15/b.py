class Cookie:
    def __init__(self, ings, quants) -> None:
        self.ings = ings
        self.quants = quants.copy()

    def score(self) -> int:
        totCap = 0
        totDur = 0
        totFla = 0
        totTex = 0
        for i in range(len(self.ings)):
            totCap += self.ings[i].cap * self.quants[i]
            totDur += self.ings[i].dur * self.quants[i]
            totFla += self.ings[i].fla * self.quants[i]
            totTex += self.ings[i].tex * self.quants[i]
        return max(0, totCap) * max(0, totDur) * max(0, totFla) * max(0, totTex)

    def totalCalories(self):
      totCal = 0
      for i in range(len(self.ings)):
          totCal += self.ings[i].cal * self.quants[i]
      return max(0, totCal)

    def better_than(self, other):
        if other is None:
            return self.totalCalories() == 500
        else:
            return self.totalCalories() == 500 and self.score() > other.score()


class Ingredient:
    def __init__(self, cap, dur, fla, tex, cal) -> None:
        self.cap = cap
        self.dur = dur
        self.fla = fla
        self.tex = tex
        self.cal = cal


def best_cookie(ings, quants, curind, avail) -> Cookie:
    if curind == len(quants) - 1:
        quants[-1] = avail
        return Cookie(ings, quants)
    if avail == 0:
        return Cookie(ings, quants)

    curBest = None
    for q in range(avail+1):
        quants[curind] = q
        c = best_cookie(ings, quants, curind + 1, avail - q)
        if c is not None and c.better_than(curBest):
            curBest = c

    return curBest


with open("in.txt", "r") as file:
    ings = []
    for line in file:
        line = line.strip().split()
        ings.append(
            Ingredient(
                int(line[2][:-1]),
                int(line[4][:-1]),
                int(line[6][:-1]),
                int(line[8][:-1]),
                int(line[10])))

    done = False
    quants = [0 for i in ings]
    c = best_cookie(ings, quants, 0, 100)
    print(c.score())
