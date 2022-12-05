file = open("i", "r")

def solve():
    line = file.readline()
    piles = []
    while line[1] != "1":
        for i in range(0, len(line), 4):
            col = i // 4
            if col >= len(piles):
                piles.append([])
            if line[i+1] != " ":
                piles[col].append(line[i+1])
        line = file.readline()
    piles = [col[::-1] for col in piles]
    file.readline()
    line = file.readline()
    while line:
        line = line.strip().split()
        n, f, t = int(line[1]), int(line[3])-1, int(line[5])-1
        to_move = piles[f][-n:]
        piles[t] += to_move
        piles[f] = piles[f][:-n]
        line = file.readline()
        
    return "".join([col[-1] for col in piles])

ans = solve()
print(ans)

file.close()