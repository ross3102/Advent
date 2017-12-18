def p1(num):
    buffer = [0]
    pos = 0
    for i in range(1, 2018):
        pos += num + 1
        pos %= len(buffer)
        buffer.insert(pos, i)
    return buffer[buffer.index(2017) + 1]

def p2(num):
    length = 0
    pos = 0
    ans = 0
    for i in range(1, 50000001):
        pos += num
        pos %= length + 1
        length += 1
        if pos == 0:
            ans = i
        pos += 1
    return ans


num = 382
print(p2(num))