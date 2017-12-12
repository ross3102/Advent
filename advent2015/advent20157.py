file = open('f', 'r')

equations = {}
results = {}

for line in file:
    line = line.split("->")
    equations[line[1].strip()] = line[0].strip().split(' ')


def calculate(letter):
    try:
        return int(letter)
    except ValueError:
        pass
    current = equations[letter]
    if letter in results:
        return results[letter]
    if len(current) > 1:
        current_op = current[-2]
        if current_op == 'RSHIFT':
            result = calculate(current[0]) >> calculate(current[-1])
        elif current_op == 'LSHIFT':
            result = calculate(current[0]) << calculate(current[-1])
        elif current_op == 'AND':
            result = calculate(current[0]) & calculate(current[-1])
        elif current_op == 'OR':
            result = calculate(current[0]) | calculate(current[-1])
        elif current_op == 'NOT':
            result = ~ calculate(current[1]) & 0xffff
        results[letter] = result
        return results[letter]
    else:
        return calculate(current[0])
print(calculate('lx'))