from functools import reduce

def XOR(v1, v2): return v1 ^ v2
def OR(v1, v2): return v1 | v2
def AND(v1, v2): return v1 & v2

OPS = {'XOR': XOR, 'OR': OR, 'AND': AND}

with open('input.txt') as f:
    info, instructions = f.read().split('\n\n')
    info = { line.split(': ')[0]: int(line.split(': ')[1]) for line in info.splitlines() }
    instructions = [tuple(line.replace('->', '').split()) for line in instructions.splitlines()]

    while instructions:
        for instru in instructions.copy():
            if instru[0] in info and instru[2] in info: 
                info[instru[3]] = OPS[instru[1]](info[instru[0]], info[instru[2]])
                instructions.remove(instru)

    info = reversed([info[k] for k in sorted(info) if k.startswith('z')])
    
    print(reduce(lambda acc, bit: (acc << 1) + bit, info))