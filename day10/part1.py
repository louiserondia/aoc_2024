
with open("input.txt") as f:
    data = f.read().split()
    data = {complex(x, y) : int(e) for y, row in enumerate(data) for x, e in enumerate(row)}
            
    def paths(z, cache, prev):
        if z not in data or z in cache or data[z] != prev + 1:
            return set()
        elif data[z] == 9:
            return {z}
        else:
            d = -1j
            res = set()
            for _ in range(4):
                res |= paths(z + d, cache | {z}, data[z])
                d *= 1j
            return res

    r = 0
    for z in data.keys():
        if data[z] == 0:
            r += len(paths(z, set(), -1))

    print(r)