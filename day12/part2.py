print("mercredi je crois aux fantomes")
cache = set()

with open("input.txt") as f:
    data = f.read().split()
    data = {complex(x, y): e for y, row in enumerate(data) for x, e in enumerate(row)}

    def rotate(m):
        x_max = int(max(p.real for p in m))
        return set(complex(z.imag, x_max - z.real) for z in m)

    def ray(m):
        f = 0
        x_max = int(max(p.real for p in m))
        y_max = int(max(p.imag for p in m))
        for x in range(x_max + 1):
            y = 0
            while y in range(y_max + 1):
                if complex(x, y) in m and complex(x, y) - 1 not in m:
                    f += 1
                    while complex(x, y) in m and complex(x, y) - 1 not in m:
                        y += 1
                else:
                    y += 1
        return f

    def grow(z, area, m):
        cache.add(z)
        m.add(z)
        for n in range(4):
            d = (1j ** n)
            if z + d in data and data[z] == data[z + d] and z + d not in cache:
                area += grow(z + d, 1, m)
        return area
    
    r = 0
    for e in data.keys():
        m = set()
        if e not in cache:
            a = grow(e, 1, m)
            faces = 0
            for _ in range(4):
                faces += ray(m)
                m = rotate(m)
            r += a * faces
    print(r)