
def traverse(data, guard, wall = complex(-1)):
    d = -1j
    path = set()
    while guard + d in data:
        if (guard, d) in path:
            return (None, 1)
        if data[guard + d] == '#' or guard + d == wall : d *= 1j
        else: 
            path.add((guard, d))
            guard += d
    return (path, 0)

def solve(data, start):
    path, _ = traverse(data, start)
    cache = set()
    res = 0
    for p, d in path:
        if (p + d) not in cache and p + d != start:
            res += traverse(data, start, p + d)[1] 
        cache.add(p + d)
    return res


with open("input.txt", 'r') as f:
    data = f.read().split("\n")
    data = {complex(x, y): e for y, row in enumerate(data) for x, e in enumerate(row)}
    start = next(i for i in data if data[i]=="^")

    print(solve(data, start))