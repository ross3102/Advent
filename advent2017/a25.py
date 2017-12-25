def p1():
    state = "A"
    steps = 12667664

    tape = {}

    cursor = 0

    for step in range(steps):
        current = tape.get(cursor, 0)
        if state == "A":
            if current == 0:
                tape[cursor] = 1
                cursor += 1
                state = "B"
            else:
                tape[cursor] = 0
                cursor -= 1
                state = "C"
        elif state == "B":
            if current == 0:
                tape[cursor] = 1
                cursor -= 1
                state = "A"
            else:
                cursor += 1
                state = "D"
        elif state == "C":
            if current == 0:
                tape[cursor] = 0
                cursor -= 1
                state = "B"
            else:
                tape[cursor] = 0
                cursor -= 1
                state = "E"
        elif state == "D":
            if current == 0:
                tape[cursor] = 1
                cursor += 1
                state = "A"
            else:
                tape[cursor] = 0
                cursor += 1
                state = "B"
        elif state == "E":
            if current == 0:
                tape[cursor] = 1
                cursor -= 1
                state = "F"
            else:
                tape[cursor] = 1
                cursor -= 1
                state = "C"
        elif state == "F":
            if current == 0:
                tape[cursor] = 1
                cursor += 1
                state = "D"
            else:
                tape[cursor] = 1
                cursor += 1
                state = "A"

    return sum(tape.values())


print(p1())