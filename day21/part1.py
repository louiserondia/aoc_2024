DIRS = { 1 : '>', 1j : 'v', -1 : '<', -1j : '^' }

def move(src, dst, pad):
    total = ''
    while src != dst:
        if src.real <  dst.real and src + 1 in pad.values(): m = 1
        elif src.imag < dst.imag and src + 1j in pad.values(): m = 1j
        elif src.real > dst.real and src - 1 in pad.values(): m = -1
        elif src.imag > dst.imag and src - 1j in pad.values(): m = -1j
        src += m
        total += DIRS[m]
    return total

with open('input.txt') as f:
    data = f.read().splitlines()
    numpad = { e : complex(x, y) for y, row in enumerate(["7,8,9", "4,5,6", "1,2,3", " ,0,A"]) for x, e in enumerate(row.split(',')) if e != ' '}
    dirpad = { e : complex(x, y) for y, row in enumerate([" ,^,A", "<,v,>"]) for x, e in enumerate(row.split(',')) if e != ' '}

    res = 0
    for l in data:
        pairs = ['A' + l[0]] + list(zip(l, l[1:]))
        moves = ''.join(move(numpad[p[0]], numpad[p[1]], numpad) + 'A' for p in pairs)
        pairs = ['A' + moves[0]] + list(zip(moves, moves[1:]))
        moves = ''.join(move(dirpad[p[0]], dirpad[p[1]], dirpad) + 'A' for p in pairs)
        pairs = ['A' + moves[0]] + list(zip(moves, moves[1:]))
        moves = ''.join(move(dirpad[p[0]], dirpad[p[1]], dirpad) + 'A' for p in pairs)
        res += len(moves) * int(l[:-1])
    print(res)

