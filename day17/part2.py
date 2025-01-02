import functools

data = open('input.txt').read().split('\n\n')
# registers = list(map(lambda l: int(l[12:]), data[0].split('\n')))
instructions = list(map(int, data[1][9:].split(',')))

def combo(i, registers):
    return [0, 1, 2, 3, registers[0], registers[1], registers[2], 7][i]

def adv(operand, registers):
    registers[0] = registers[0] // 2 ** combo(operand, registers)

def bxl(operand, registers):
    registers[1] = registers[1] ^ operand

def bst(operand, registers):
    registers[1] = combo(operand, registers) % 8

def jnz(operand, registers):
    return operand if registers[0] else None

def bxc(_, registers):
    registers[1] = registers[1] ^ registers[2]

def out(operand, registers):
    print(combo(operand, registers) % 8, end=',')

def bdv(operand, registers):
    registers[1] = registers[0] // 2 ** combo(operand, registers)

def cdv(operand, registers):
    registers[2] = registers[0] // 2 ** combo(operand, registers)

OPS = { 0 : adv, 1 : bxl, 2 : bst, 3 : jnz, 4 : bxc, 5 : out, 6 : bdv, 7 : cdv }

def check(registers):
    ip = 0
    
    while ip < len(instructions):
        if (ret := OPS[instructions[ip]](instructions[ip + 1], registers)) is not None: 
            ip = ret
        else:
            ip += 2

def f(a):
    b = c = 0
    t = []
    while a > 0:
        b = a & 0b111
        b = b ^ 0b101
        c = a >> b
        b = b ^ c
        b = b ^ 0b110
        a = a >> 3
        t.append(b & 0b111)
    return t

@functools.cache
def b(a: int, i: int):
    out = f(a)
    if out == instructions: return a
    if out[:i] != instructions[:i]: return None
    res = None
    for n in range(1 << 10):
        na = a | (n << (i * 3))
        nres = b(na, i + 1)
        if nres is not None: res = min(res or nres, nres)
    return res

print(b(0, 0))