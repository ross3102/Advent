orig = open("f", "r")
file = [line for line in orig][0]

end = ""

i = 0

while i < len(file):
    if file[i] == "(":
        end_paren = file[i:].index(")") + i
        x = file[i:].index("x") + i
        thing = file[i:end_paren + 1]
        num1 = int(file[i + 1:x])
        num2 = int(file[x + 1:end_paren])
        for j in range(num2):
            end += file[end_paren + 1:end_paren + 1 + num1]
        i += len(thing) + num1
    else:
        i+=1

print(end)