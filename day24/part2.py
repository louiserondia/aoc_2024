import operator
from itertools import combinations
import random

OPS = {'XOR': operator.xor, 'OR': operator.or_, 'AND': operator.and_}

def routine(instructions, info, swaps):
    while instructions:
        executed = set()
        for instru in instructions:
            out = instru[3]
            if instru[0] in info and instru[2] in info: 
                if instru[3] in swaps:
                    out = swaps[instru[3]]
                info[out] = OPS[instru[1]](info[instru[0]], info[instru[2]])
                executed.add(instru)
        if not executed:
            break
        instructions.difference_update(executed)

    info = reversed([str(info[k]) for k in sorted(info) if k.startswith('z')])
    return ''.join(info)

def find_no_no():
    sure = []
    maybe = []
    for instru in instructions:
        if instru[3].startswith('z') and instru[3] != 'z00' and instru[3] != 'z45' and instru[1] != 'XOR':
            sure.append(instru[3])
        elif (instru[0].startswith('x') or instru[0].startswith('y')) and instru[0][1:] != '00' and instru[0][1:] != '45' and instru[1] == 'XOR':
            nexts = [i for i in instructions if i[0] == instru[3] or i[2] == instru[3]]
            if all(n[1] != 'XOR' for n in nexts):
                sure.append(instru[3])
                missing_z = next(i for i in instructions if i[3] == ('z' + instru[0][1:]))
                maybe.append((missing_z[0], missing_z[2]))
            else:
                nexts = next(n for n in nexts if n[1] == 'XOR')
                if not nexts[3].startswith('z'):
                    maybe.append((instru[3], nexts[3]))
    return sure, maybe

def gen_bit():
    rx = random.getrandbits(45)
    ry = random.getrandbits(45)
    bx = f"{rx:045b}"
    by = f"{ry:045b}"
    d = {f"x{44 - i:02}": int(bit) for i, bit in enumerate(bx)}
    d.update({f"y{44 - i:02}": int(bit) for i, bit in enumerate(by)})
    return rx, ry, d


with open('input.txt') as f:
    info, instructions = f.read().split('\n\n')
    info = { line.split(': ')[0]: int(line.split(': ')[1]) for line in info.splitlines() }
    instructions = set(tuple(line.replace('->', '').split()) for line in instructions.splitlines())

    rx, ry, info = gen_bit()
    target = bin(int(rx) + int(ry))[2:]

    res = routine(instructions.copy(), info.copy(), {})
    print('res    -> ', int(res, 2))
    print('target -> ', int(target, 2))

    sure, maybe = find_no_no()

    duos = set()
    for s in sure:
        for m in maybe:
            duos.add((s, m[0]))
            duos.add((s, m[1]))
    
    cache = set()
    for quatuor in combinations(duos, 4):
        wires = set(e for q in quatuor for e in q)
        if len(wires) != 8:
            continue
        wd = {}
        for q in quatuor:
            wd[q[0]] = q[1]
            wd[q[1]] = q[0]
        res = routine(instructions.copy(), info.copy(), wd)
        if int(res, 2) == int(target, 2):
            cache.add(quatuor)
    print(cache)


    for c in set(cache):
        wd = {}
        for q in quatuor:
            wd[q[0]] = q[1]
            wd[q[1]] = q[0]
        for _ in range(100):
            rx, ry, info = gen_bit()
            target = rx + ry
            res = routine(instructions.copy(), info, wd)
            if c in cache:
                cache.remove(c)

    print(cache)