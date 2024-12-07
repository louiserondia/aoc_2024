def s(data, guard):
    d = -1j
    r = {guard}
    while guard + d in data:
        if data[guard + d] == '#': d *= 1j
        guard += d
        r.add(guard)
    return len(r)

with open("input.txt", 'r') as f:
    data = f.read().split("\n")
    data = {complex(x, y): e for y, row in enumerate(data) for x, e in enumerate(row)}
    start = next(i for i in data if data[i]=="^")

    print(s(data, start))
