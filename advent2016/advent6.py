file =open('f', 'r')

message = []
newfile = []
for line in file:
    newfile.append(line)
for i in range(8):
    chars = []
    counts = []
    for line in newfile:
        chars.append(line[i])
    for char in chars:
        counts.append(chars.count(char))
    message.append(chars[counts.index(min(counts))])
print("The message is", "".join(message))