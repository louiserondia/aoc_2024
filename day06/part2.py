
def p(data, guard, wall):
    d = -1j
    path = set((guard, d))
    while guard + d in data:
        if (guard, d) in path:
            return 1
        path.add((guard, d))
        if data[guard + d] == '#' or guard + d == wall: d *= 1j
        else: guard += d
    return 0

def solve(data, guard):
    d = -1j
    res = set()
    p0 = guard
    while guard + d in data:
        if data[guard + d] == "#": 
            d *= 1j
        else:
            guard += d
            if (guard not in res) and p(data, p0, guard):
                res.add(guard)
    return res


with open("input.txt", 'r') as f:
    data = f.read().split("\n")
    data = {complex(x, y): e for y, row in enumerate(data) for x, e in enumerate(row)}
    start = next(i for i in data if data[i]=="^")

    r = solve(data, start)
    print(r, len(r))