class Program:
    def __init__(self, id, prog):
        self.registers = {"p": id}
        self.pos = 0
        self.waiting = False
        self.otherProg = prog
        self.input = []
        self.sent = 0

    def runInstruction(self, file):
        if not self.waiting:
            line = file[self.pos]
            line = line.strip().split(" ")
            instruction = line[0]
            params = line[1:]

            if instruction == "snd":
                checkExists(params[0], self.registers)
                toSend = int(self.registers.get(params[0], params[0]))
                self.sent += 1
                self.otherProg.input.append(toSend)
            elif instruction == "set":
                toR = params[0]
                fromR = params[1]

                checkExists(fromR, self.registers)

                self.registers[toR] = int(self.registers.get(fromR, fromR))
            elif instruction == "add":
                toR = params[0]
                fromR = params[1]

                checkExists(fromR, self.registers)
                checkExists(toR, self.registers)

                self.registers[toR] += int(self.registers.get(fromR, fromR))
            elif instruction == "mul":
                toR = params[0]
                fromR = params[1]

                checkExists(fromR, self.registers)
                checkExists(toR, self.registers)

                self.registers[toR] *= int(self.registers.get(fromR, fromR))
            elif instruction == "mod":
                toR = params[0]
                fromR = params[1]

                checkExists(fromR, self.registers)
                checkExists(toR, self.registers)

                self.registers[toR] %= int(self.registers.get(fromR, fromR))
            elif instruction == "rcv":
                var = params[0]

                if len(self.input) > 0:
                    self.registers[var] = self.input[0]
                    del self.input[0]
                else:
                    self.waiting = var
            elif instruction == "jgz":
                var = params[0]
                offset = params[1]

                checkExists(var, self.registers)
                checkExists(offset, self.registers)

                if int(self.registers.get(var, var)) > 0:
                    self.pos += int(self.registers.get(offset, offset)) - 1
            self.pos += 1
        else:
            if len(self.input) > 0:
                self.registers[self.waiting] = self.input[0]
                del self.input[0]
                self.waiting = False


def p2(file):
    program0 = Program(0, None)
    program1 = Program(1, program0)
    program0.otherProg = program1
    while not (program0.waiting and program1.waiting):
        program0.runInstruction([i for i in file])
        program1.runInstruction([i for i in file])
    return program1.sent


def checkExists(item, registers):
    try:
        int(item)
    except:
        if not registers.get(item, False):
            registers[item] = 0


def p1(file):
    registers = {}
    instructions = [i.strip().split(" ") for i in file]

    output = []
    line = 0

    while line < len(instructions):
        instruction = instructions[line][0]
        params = instructions[line][1:]

        if instruction == "snd":
            checkExists(params[0], registers)

            output.append(int(registers.get(params[0], params[0])))
        elif instruction == "set":
            toR = params[0]
            fromR = params[1]

            checkExists(fromR, registers)

            registers[toR] = int(registers.get(fromR, fromR))
        elif instruction == "add":
            toR = params[0]
            fromR = params[1]

            checkExists(fromR, registers)
            checkExists(toR, registers)

            registers[toR] += int(registers.get(fromR, fromR))
        elif instruction == "mul":
            toR = params[0]
            fromR = params[1]

            checkExists(fromR, registers)
            checkExists(toR, registers)

            registers[toR] *= int(registers.get(fromR, fromR))
        elif instruction == "mod":
            toR = params[0]
            fromR = params[1]

            checkExists(fromR, registers)
            checkExists(toR, registers)

            registers[toR] %= int(registers.get(fromR, fromR))
        elif instruction == "rcv":
            var = params[0]

            checkExists(var, registers)

            if int(registers.get(var, var)) != 0:
                return output[-1]
        elif instruction == "jgz":
            var = params[0]
            offset = params[1]

            checkExists(var, registers)
            checkExists(offset, registers)

            if int(registers.get(var, var)) > 0:
                line += int(registers.get(offset, offset))
                continue
        line += 1

file = list(open("f.txt", "r"))
print(p2(file))