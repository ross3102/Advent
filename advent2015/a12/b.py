import json


def extract(js):
    if isinstance(js, int):
        return js
    elif isinstance(js, str):
        return 0
    elif isinstance(js, dict):
        total = 0
        for child in js.values():
            if child == "red":
                return 0
            total += extract(child)
        return total
    else:  # List
        total = 0
        for child in js:
            total += extract(child)
        return total


with open("in.txt", "r") as file:
    js = json.loads(file.readline())
    print(extract(js))
