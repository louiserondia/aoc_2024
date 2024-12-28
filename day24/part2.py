import random
import operator
from itertools import combinations

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
    for (x, op, _, z) in instructions:
        if z.startswith('z') and z != 'z00' and z != 'z45' and op != 'XOR':
            sure.append(z)
        elif (x.startswith('x') or x.startswith('y')) and int(x[1:]) not in (0, 45) and op == 'XOR':
            nexts = [i for i in instructions if i[0] == z or i[2] == z]
            if all(n[1] != 'XOR' for n in nexts):
                sure.append(z)
                missing_z = next(i for i in instructions if i[3] == ('z' + x[1:]))
                maybe.append((missing_z[0], missing_z[2]))
            else:
                nexts = next(n for n in nexts if n[1] == 'XOR')
                if not nexts[3].startswith('z'):
                    maybe.append((z, nexts[3]))
    return sure, maybe

def gen_bit():
    rx, ry = random.getrandbits(45), random.getrandbits(45)
    bx, by = f"{rx:045b}", f"{ry:045b}"
    d = {f"x{44 - i:02}": int(bit) for i, bit in enumerate(bx)}
    d.update({f"y{44 - i:02}": int(bit) for i, bit in enumerate(by)})
    return rx, ry, d


with open('input.txt') as f:
    info, instructions = f.read().split('\n\n')
    info = { line.split(': ')[0]: int(line.split(': ')[1]) for line in info.splitlines() }
    instructions = set(tuple(line.replace('->', '').split()) for line in instructions.splitlines())
    sure, maybe = find_no_no()
    duos = {(s, m[i]) for s in sure for m in maybe for i in (0, 1)}
    
    for quatuor in combinations(duos, 4):
        wires = set(e for q in quatuor for e in q)
        if len(wires) != 8: continue

        wd = {}
        for q in quatuor:
            wd[q[0]] = q[1]
            wd[q[1]] = q[0]
        for i in range(100):
            rx, ry, info = gen_bit()
            target = rx + ry
            res = routine(instructions.copy(), info.copy(), wd)
            if int(res, 2) != int(target):
                break
        else:
            print(','.join(sorted(wires)))
