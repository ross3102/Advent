from hashlib import md5
inp = "bgvyzdsv"
# total = 0
number = 0
# code = 0
# seen = []
found = False
print("DECODING...")
while not found:
    string = inp + str(number)
    m = md5(string.encode()).hexdigest()
    if m[:6] == "000000":
        found = True
        # if m[5] not in seen:
        #     code[int(m[5])] = m[6]
        #     total += 1
        # seen.append(m[5])
    else:
        number += 1

print("The code is:", number)