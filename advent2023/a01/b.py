from os import path
file = open(path.dirname(__file__) + "/i", "r")

digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def solve():
    ans = 0
    for line in file:
        line = line.strip()
        ints = []
        for i in range(len(line)):
            try:
                for di in range(len(digits)):
                    d = digits[di]
                    if line[i:].startswith(d):
                        ints.append(str(di))
                ints.append(str(int(line[i])))
            except:
                pass
        ans += int(ints[0] + ints[-1])
    return ans

ans = solve()
print(ans)

file.close()