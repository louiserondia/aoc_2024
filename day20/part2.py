def md(z1, z2):
    return abs(z1.real - z2.real) + abs(z1.imag - z2.imag)

def traverse(data):
    cache = {}
    res = 0
    def get_path():
        path = []        
        p = next(k for k, v in data.items() if v =='S')
        d = 1
        while data[p] != 'E':
            cache[p] = len(path)
            path.append(p)
            if data[p + d] == '#':
                d = d * 1j if data[p + d * 1j] != '#' else d * -1j
            p += d
            
        cache[p] = len(path)
        return path

    path = get_path()
    for p in path:
        # print(p, res)
        cheats = filter(lambda z: z in cache and md(z, p) <= 20 , data.keys())
        for c in cheats: 
            if (cache[c] - cache[p]) - md(c, p) >= 100: res += 1
    return res

with open('input.txt') as f:
    data = f.read().splitlines()
    data = { complex(x, y) : e for y, row in enumerate(data) for x, e in enumerate(row) }
    print(traverse(data))