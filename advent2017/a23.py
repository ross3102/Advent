def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True


#  Note: This solution is specific to the puzzle input
def p2():
    return len([1 for b in range(108100, 125101, 17) if not isPrime(b)])


def p1(file):
    registers = {}
    for l in "abcdefgh":
        registers[l] = 0
    instructions = [i.strip().split(" ") for i in file]

    total = 0
    line = 0

    while line < len(instructions):
        instruction = instructions[line][0]
        params = instructions[line][1:]

        if instruction == "set":
            toR = params[0]
            fromR = params[1]

            registers[toR] = int(registers.get(fromR, fromR))
        elif instruction == "sub":
            toR = params[0]
            fromR = params[1]

            registers[toR] -= int(registers.get(fromR, fromR))
        elif instruction == "mul":
            toR = params[0]
            fromR = params[1]
            total += 1

            registers[toR] *= int(registers.get(fromR, fromR))
        elif instruction == "jnz":
            var = params[0]
            offset = params[1]

            if int(registers.get(var, var)) != 0:
                line += int(registers.get(offset, offset))
                continue
        line += 1
    return total

file = list(open("f.txt", "r"))
print(p2())