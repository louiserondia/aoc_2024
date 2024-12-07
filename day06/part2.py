
def p(data, guard, path, d):
    while guard + d in data:
        if data[guard + d] == '#': d *= 1j
        else:
            guard += d
            if (guard, d) in path or ((guard, d * 1j) in path and data[guard + d] == '#'):
                return 1
    return 0

def s(data, guard):
    d = -1j
    path = set()
    r = 0
    while guard + d in data:
        if data[guard + d] == '#': d *= 1j
        else:
            path.add((guard, d))
            r += p(data, guard, path, d * 1j)
            guard += d
    return r

with open("input.txt", 'r') as f:
    data = f.read().split("\n")
    data = {complex(x, y): e for y, row in enumerate(data) for x, e in enumerate(row)}
    start = next((i for i in data if data[i]=="^"), None)

    print(s(data, start))