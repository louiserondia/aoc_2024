
data = open('input.txt').read().split('\n\n')
registers = list(map(lambda l: int(l[12:]), data[0].split('\n')))
instructions = list(map(int, data[1][9:].split(',')))
ip = 0

def combo(i):
    return [0, 1, 2, 3, registers[0], registers[1], registers[2], 7][i]

def adv(operand):
    registers[0] = registers[0] // 2 ** combo(operand)
    # division into register A with numerator = A register and denominator = 2 ** combo operand

def bxl(operand):
    registers[1] = registers[1] ^ operand
    # bitwise XOR of register B and the instruction's literal operand to register B.

def bst(operand):
    registers[1] = combo(operand) % 8
    # combo operand modulo 8 to the B register.

def jnz(operand):
    if registers[0]:
        return operand
    # nothing if the A register is 0. else, jumps with instruction pointer to literal operand

def bxc(_):
    registers[1] = registers[1] ^ registers[2]
    # bitwise XOR of register B and register C into register B. 

def out(operand):
    print(combo(operand) % 8, end=',')
    # combo operand modulo 8, then outputs that value.

def bdv(operand):
    registers[1] = registers[0] // 2 ** combo(operand)
    # adv stored in register B

def cdv(operand):
    registers[2] = registers[0] // 2 ** combo(operand)
    # adv stored in register C

OPS = { 0 : adv, 1 : bxl, 2 : bst, 3 : jnz, 4 : bxc, 5 : out, 6 : bdv, 7 : cdv }

while ip < len(instructions):
    if (ret := OPS[instructions[ip]](instructions[ip + 1])) is not None: 
        ip = ret
    else:
        ip += 2



