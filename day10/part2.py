
with open("input.txt") as f:
    data = f.read().split()
    data = {complex(x, y) : int(e) for y, row in enumerate(data) for x, e in enumerate(row)}
            
    def paths(z, cache, prev):
        if z not in data or z in cache or data[z] != prev + 1:
            return 0
        elif data[z] == 9:
            return 1
        else:
            return sum(paths(z + (1j ** n), cache | {z}, data[z]) for n in range(4))

    r = 0
    for z in data.keys():
        if data[z] == 0:
            r += paths(z, set(), -1)

    print(r)