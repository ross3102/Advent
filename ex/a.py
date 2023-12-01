from os import path
file = open(path.dirname(__file__) + "/i", "r")

def solve():
    ans = 0
    for line in file:
        line = line.strip()
        
    return ans

ans = solve()
print(ans)

file.close()