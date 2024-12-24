from itertools import count

def cheat(score, p, cache):
    if p in cache and cache[p] > score: return cache[p] - score
    t = []
    for d in [1j, -1j, 1, -1]:
        if p + d in cache and cache[p + d] > score + 1:
            t.append(cache[p + d] - score - 1)
    return t

def traverse(data):
    cache = {}
    res = []
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
        for nd in [1j, -1j, 1, -1]:
            if p + nd in data and data[p + nd] == '#' and p + nd not in res:
                res += cheat(cache[p] + 1, p + nd, cache)
    return len(path), res

with open('input.txt') as f:
    data = f.read().splitlines()
    data = { complex(x, y) : e for y, row in enumerate(data) for x, e in enumerate(row) }

    score, res = traverse(data)
    i = sum(r >= 100 for r in res)
    print(i)