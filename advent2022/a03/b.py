file = open("i", "r")

def solve():
    ans = 0
    lines = [line.strip() for line in file]
    for i in range(0, len(lines) - 2, 3):
        for c in lines[i]:
            if c in lines[i+1] and c in lines[i+2]:
                if c == c.lower():
                    ans += ord(c) - ord('a') + 1
                else:
                    ans += ord(c) - ord('A') + 27
                break
    return ans

ans = solve()
print(ans)

file.close()