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

with open('input.txt') as f:
    info, instructions = f.read().split('\n\n')
    info = { line.split(': ')[0]: int(line.split(': ')[1]) for line in info.splitlines() }
    instructions = set(tuple(line.replace('->', '').split()) for line in instructions.splitlines())




    res = routine(instructions.copy(), info.copy(), {})
    x = ''.join(reversed([str(info[k]) for k in sorted(info) if k.startswith('x')]))
    y = ''.join(reversed([str(info[k]) for k in sorted(info) if k.startswith('y')]))    
    target = int(x, 2) + int(y, 2)
    
    # print('        ', int(res, 2))
    # print('target :', target)

    # if int(res, 2) == target:
    #     print(' ---> BON <---')
    # else:
    #     print(res)
    print('       ', bin(target)[2:])
    cache = set()
    # duos =  combinations(fucking_res, 2)

    
    # for duos_4 in combinations(duos, 1):
    # wires = set(e for d in duos_4 for e in d)
    # if len(wires) != 2 and any(e not in wires for e in []):
    #     continue

    wd = {'qcw': 'hqc', 'z11': 'hcc', 'z35': 'fdw', 'bpf': 'z05', 
          'hqc': 'qcw', 'hcc': 'z11', 'fdw': 'z35', 'z05': 'bpf'}
    # for d in duos_4:
    #     wd[d[0]] = d[1]
    #     wd[d[1]] = d[0]
    res = routine(instructions.copy(), info.copy(), wd)
    if int(res, 2) == target:
        # cache.add(tuple(duos_4))
        print('lets go', res)
        # print(duos_4)
    # print(cache)
