def p1(steps):
    lets = [i for i in "abcdefghijklmnop"]
    for step in steps:
        instruction = step[0]
        if instruction == "s":
            num = int(step[1:])
            lets = lets[-num:] + lets[:-num]
        elif instruction == "x":
            nums = [int(i) for i in step[1:].split("/")]
            temp = lets[nums[0]]
            lets[nums[0]] = lets[nums[1]]
            lets[nums[1]] = temp
        elif instruction == "p":
            nums = step[1:].split("/")
            i1 = lets.index(nums[0])
            i2 = lets.index(nums[1])
            temp = lets[i1]
            lets[i1] = lets[i2]
            lets[i2] = temp
    return "".join(lets)

def p2(steps):
    lets = [i for i in "abcdefghijklmnop"]
    for dance in range(1000000000 % 48):
        for step in steps:
            instruction = step[0]
            if instruction == "s":
                num = int(step[1:])
                lets = lets[-num:] + lets[:-num]
            elif instruction == "x":
                nums = [int(i) for i in step[1:].split("/")]
                temp = lets[nums[0]]
                lets[nums[0]] = lets[nums[1]]
                lets[nums[1]] = temp
            elif instruction == "p":
                nums = step[1:].split("/")
                i1 = lets.index(nums[0])
                i2 = lets.index(nums[1])
                temp = lets[i1]
                lets[i1] = lets[i2]
                lets[i2] = temp
    return "".join(lets)

steps = list(open("f.txt", "r"))[0].split(",")
print(p2(steps))
