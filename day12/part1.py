print("mercredi je crois aux fantomes")
cache = set()

def change_perim(z):
    n = sum(1 for i in range(4) if z + (1j ** i) in cache and data[z] == data[z + (1j ** i)])
    return 4 - (n * 2)

with open("input.txt") as f:
    data = f.read().split()
    data = {complex(x, y): e for y, row in enumerate(data) for x, e in enumerate(row)}

    def grow(z, area, perim):
        cache.add(z)
        for n in range(4):
            d = (1j ** n)
            if z + d in data and data[z] == data[z + d] and z + d not in cache:
                a, p = grow(z + d, 1, change_perim(z + d))
                area += a
                perim += p
        return area, perim
    
    r = 0
    for e in data.keys():
        if e not in cache:
            a, p = grow(e, 1, 4)
            r += a * p
    print(r)