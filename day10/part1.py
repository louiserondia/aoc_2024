
with open("input.txt") as f:
    data = f.read().split()
    data = {complex(x, y) : int(e) for y, row in enumerate(data) for x, e in enumerate(row)}
            
    def paths(z, cache, prev):
        if z not in data or z in cache or data[z] != prev + 1:
            return set()
        elif data[z] == 9:
            return {z}
        else:
            return set().union(*(paths(z + (1j ** n), cache | {z}, data[z]) for n in range(4)))
        
    r = sum(len(paths(z, set(), -1)) for z in data.keys() if data[z] == 0)
    print(r)