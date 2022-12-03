file = open("i", "r")

def solve():
    ans = 0
    for line in file:
        line = line.strip()
        a = line[:len(line)//2]
        b = line[len(line)//2:]
        for c in a:
            if c in b:
                if c == c.lower():
                    ans += ord(c) - ord('a') + 1
                else:
                    ans += ord(c) - ord('A') + 27
                break
    return ans

ans = solve()
print(ans)

file.close()