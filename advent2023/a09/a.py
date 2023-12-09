from os import path
file = open(path.dirname(__file__) + "/i", "r")

def solve():
    ans = 0
    for line in file:
        line = line.strip()
        nums = list(map(int, line.split()))
        seqs = [nums]
        tot = 0
        while not all(x == 0 for x in seqs[-1]):
            tot += seqs[-1][-1]
            l = seqs[-1]
            nxt = [l[i+1]-l[i] for i in range(len(l)-1)]
            seqs.append(nxt)
        ans += tot
    return ans

ans = solve()
print(ans)

file.close()