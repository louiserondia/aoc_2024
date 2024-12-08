from itertools import permutations

with open("input.txt") as f:
    data = f.read().split()
    w, h = len(data[0]), len(data)
    data = {complex(x, y) : e for y, row in enumerate(data) for x, e in enumerate(row) if e != '.'}

    cache = set()
    for (z1, z2) in permutations(data, 2):
        if data[z1] == data[z2]:
            d = z1 - z2
            for dir in (1, -1):
                z = z1
                while z.real in range(w) and z.imag in range(h):
                    cache.add(z)
                    z += d * dir
                    
    print(len(cache))