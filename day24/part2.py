import random, operator
from itertools import combinations

OPS = {'XOR': operator.xor, 'OR': operator.or_, 'AND': operator.and_}

def routine(instructions, info, swaps):
    while instructions:
        executed = set()
        for (x, op, y, z) in instructions:
            if x in info and y in info: 
                info[swaps.get(z, z)] = OPS[op](info[x], info[y])
                executed.add((x, op, y, z))
        if not executed:
            break
        instructions.difference_update(executed)

    return ''.join(reversed([str(info[k]) for k in sorted(info) if k.startswith('z')]))

def find_no_no():
    sure, maybe = [], []
    for (x, op, _, z) in instructions:
        if z.startswith('z') and z not in ('z00', 'z45') and op != 'XOR':
            sure.append(z)
        elif x.startswith(('x', 'y')) and int(x[1:]) not in (0, 44) and op == 'XOR':
            nexts = [i for i in instructions if i[0] == z or i[2] == z]
            if all(n[1] != 'XOR' for n in nexts):
                sure.append(z)
                missing_z = next(i for i in instructions if i[3] == ('z' + x[1:]))
                maybe.append((missing_z[0], missing_z[2]))
            else:
                next_xor = next(n for n in nexts if n[1] == 'XOR')[3]
                if not next_xor.startswith('z'):
                    maybe.append((z, next_xor))
    return sure, maybe

def gen_bit():
    rx, ry = random.getrandbits(45), random.getrandbits(45)
    bx, by = f"{rx:045b}", f"{ry:045b}"
    d = {f"x{44 - i:02}": int(bit) for i, bit in enumerate(bx)}
    d.update({f"y{44 - i:02}": int(bit) for i, bit in enumerate(by)})
    return rx, ry, d


with open('input.txt') as f:
    instructions = f.read().split('\n\n')[1]
    instructions = set(tuple(line.replace('->', '').split()) for line in instructions.splitlines())
    sure, maybe = find_no_no()
    duos = {(s, m[i]) for s in sure for m in maybe for i in (0, 1)}
    
    for quatuor in combinations(duos, 4):
        wires = set(e for q in quatuor for e in q)
        if len(wires) != 8: continue

        wd = {}
        for q in quatuor:
            wd[q[0]], wd[q[1]] = q[1], q[0]
        for i in range(50):
            rx, ry, info = gen_bit()
            target = rx + ry
            res = routine(instructions.copy(), info.copy(), wd)
            if int(res, 2) != int(target): break
        else:
            print(','.join(sorted(wires)))
            break
