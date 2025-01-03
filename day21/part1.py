DIRS = { 1 : '>', 1j : 'v', -1 : '<', -1j : '^' }

def md(z1, z2):
    return abs(z1.real - z2.real) + abs(z1.imag - z2.imag)

def move(src, dst, pad, current, res, cache):
    if src == dst:
        res.add(current)
        return res
    elif src not in pad.values() or src in cache:
        return None
    m = md(src, dst)
    cache.append(src)
    dirs = [d for d in [1, 1j, -1, -1j] if md(src + d, dst) <= m]
    for d in dirs:
        moves = move(src + d, dst, pad, current + DIRS[d], res, [] + cache)
        if moves is not None:
            res.update(moves)
    return res

def compute(ops, pads, current):
    if not ops: return current
    
    current = 'A' + current
    pad = pads[ops[0]]
    pairs = list(zip(current, current[1:]))
    res = ''
    line = [move(pad[p[0]], pad[p[1]], pad, '', set(), []) for p in pairs]
    for l in line:
        rm = min((compute(ops[1:], pads, m + 'A') for m in l), key=len)
        res += rm
    return res

with open('input.txt') as f:
    data = f.read().splitlines()
    numpad = { e : complex(x, y) for y, row in enumerate(["7,8,9", "4,5,6", "1,2,3", " ,0,A"]) for x, e in enumerate(row.split(',')) if e != ' '}
    dirpad = { e : complex(x, y) for y, row in enumerate([" ,^,A", "<,v,>"]) for x, e in enumerate(row.split(',')) if e != ' '}

    r = 0
    for d in data:
        res = compute([0, 1, 1], [numpad, dirpad], d)
        r += len(res) * int(d[:-1])

    print(r)
