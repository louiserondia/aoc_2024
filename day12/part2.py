print("mercredi je crois aux fantomes")
cache = set()
DIRS = [1j, 1, -1j, -1]

with open("input.txt") as f:
    data = f.read().split()
    data = {complex(x, y): e for y, row in enumerate(data) for x, e in enumerate(row)}

    def calculate_faces(z, m, d, score, c):
        if z + d in c or (z == min(m, key=lambda z1: abs(z1)) and score):
            return 0
        penality = 0
        while z + d not in m:
            d *= 1j
            penality += 1
        if all(z + d in m for d in DIRS):
            d *= -1j
            penality += 1
        c.add((z, d))
        score += calculate_faces(z + d, m, d, score + penality, c)
        return score    

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
        if e not in cache:
            m = set()
            a = grow(e, 1, m)
            if len(m) == 1:
                r += a * 4
            else:
                start = min(m, key=lambda z: abs(z))
                first_d = list(filter(lambda d: start + d in m and any((start + d2) not in m for d2 in DIRS), DIRS))
                faces = calculate_faces(start, m, first_d[0], 0, set())
                print(faces)
                r += a * faces
    print(r)