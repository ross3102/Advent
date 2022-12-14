file = open("i", "r")

def less(left, right):
    if type(left) == list:
        if type(right) == list:
            ll = len(left)
            lr = len(right)
            i = 0
            while i < ll:
                if i >= lr:
                    return False
                curisless = less(left[i], right[i])
                if curisless is not None:
                    return curisless
                i += 1
            if i < lr:
                return True
            return None
        else:
            return less(left, [right])
    else:
        if type(right) == list:
            return less([left], right)
        else:
            if left == right:
                return None
            return left < right

def solve():
    ans = 0
    line = file.readline()
    i = 1
    while line:
        line = line.strip()
        lst1 = eval(line)
        line = file.readline().strip()
        lst2 = eval(line)
        file.readline()
        line = file.readline()
        if less(lst1, lst2):
            ans += i
        i += 1
    return ans

ans = solve()
print(ans)

file.close()