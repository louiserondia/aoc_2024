import operator

OPS = {'XOR': operator.xor, 'OR': operator.or_, 'AND': operator.and_}

with open('input.txt') as f:
    info, instructions = f.read().split('\n\n')
    info = { line.split(': ')[0]: int(line.split(': ')[1]) for line in info.splitlines() }
    instructions = [tuple(line.replace('->', '').split()) for line in instructions.splitlines()]

    while instructions:
        for instru in instructions.copy():
            if instru[3] in info: continue
            if instru[0] in info and instru[2] in info: 
                info[instru[3]] = OPS[instru[1]](info[instru[0]], info[instru[2]])
                instructions.remove(instru)

    info = reversed([str(info[k]) for k in sorted(info) if k.startswith('z')])
    print(int(''.join(info), 2))