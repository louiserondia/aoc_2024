
data = open('input.txt').read().split('\n\n')
registers = list(map(lambda l: int(l[12:]), data[0].split('\n')))
instructions = list(map(int, data[1][9:].split(',')))

def combo(i):
    return [0, 1, 2, 3, registers[0], registers[1], registers[2], 7][i]

def adv(operand, reste):
    registers[0] = reste + registers[0] * 2 ** combo(operand)

def bxl(operand):
    registers[1] = registers[1] ^ operand

def bst(operand):
    registers[1] = combo(operand) % 8

def bxc():
    registers[1] = registers[1] ^ registers[2]

def out(operand):
    return combo(operand) % 8

def cdv(operand):
    registers[2] = registers[0] // 2 ** combo(operand)

def compute(reste_a):
    adv(3, reste_a)
    bxl(6)
    bxc()
    cdv(5)
    bxl(5)
    bst(4)
    return out(5)

i = len(instructions)
while i >= 0:
    i -= 1
    comp = compute(instructions[i])
    print(comp)
    print(registers)
