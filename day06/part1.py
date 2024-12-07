from collections import defaultdict
DIRS = [-1j, 1, 1j, -1]

def s(data, guard):
    d = 0
    r = {guard}
    while guard + DIRS[d] in data:
        if data[guard + DIRS[d]] == '#': d = (d + 1) % 4
        else:
            guard += DIRS[d]
            r.add(guard)
    return len(r)

with open("input.txt", 'r') as f:
    data = f.read().split("\n")
    data = {complex(x, y): e for y, row in enumerate(data) for x, e in enumerate(row)}
    start = next((i for i in data if data[i]=="^"), None)

    print(s(data, start))
