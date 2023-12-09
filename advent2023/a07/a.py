from os import path
from functools import cmp_to_key
file = open(path.dirname(__file__) + "/i", "r")

ranks = "23456789TJQKA"

def val(c):
    return ranks.index(c)

def score(hand):
    counts = {}
    for c in hand:
        counts[c] = hand.count(c)
    parsed = []
    for k in counts:
        parsed.append((val(k), counts[k]))
    parsed.sort(key=lambda p: -p[1])
    
    if parsed[0][1] == 5:
        return 6
    elif parsed[0][1] == 4:
        return 5
    elif parsed[0][1] == 3 and parsed[1][1] == 2:
        return 4
    elif parsed[0][1] == 3:
        return 3
    elif parsed[0][1] == 2 and parsed[1][1] == 2:
        return 2
    elif parsed[0][1] == 2:
        return 1
    else:
        return 0
    
def cmp(hb1, hb2):
    h1 = hb1[0]
    h2 = hb2[0]
    s1 = score(h1)
    s2 = score(h2)
    if s1 < s2:
        return -1
    elif s1 > s2:
        return 1
    
    for i in range(len(h1)):
        v1 = val(h1[i])
        v2 = val(h2[i])
        if v1 < v2:
            return -1
        elif v2 < v1:
            return 1
    return 0

def solve():
    ans = 0
    hands = []
    for line in file:
        line = line.strip()
        hand, bid = line.split()
        bid = int(bid)
        hands.append((hand, bid))
    hands.sort(key=cmp_to_key(cmp))
    for i in range(len(hands)):
        ans += (i+1) * hands[i][1]
    return ans

ans = solve()
print(ans)

file.close()