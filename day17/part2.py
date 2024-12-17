
data = open('input.txt').read().split('\n\n')
registers = list(map(lambda l: int(l[12:]), data[0].split('\n')))
instructions = list(map(int, data[1][9:].split(',')))

def combo(i):
    return [0, 1, 2, 3, registers[0], registers[1], registers[2], 7][i]

def adv(operand):
    registers[0] = registers[0] // 2 ** combo(operand)
    # division into register A with numerator = A register and denominator = 2 ** combo operand

def adv_1(operand, reste):
    registers[0] = reste + registers[0] * 2 ** combo(operand)

def bxl(operand):
    registers[1] = registers[1] ^ operand
    # bitwise XOR of register B and the instruction's literal operand to register B.

def bst(operand):
    registers[1] = combo(operand) % 8
    # combo operand modulo 8 to the B register.

def bst_1(operand, n):
    registers[1] = combo(operand) * 8 * n + registers[1]

def jnz(operand):
    return operand if registers[0] else None
    # nothing if the A register is 0. else, jumps with instruction pointer to literal operand

def bxc(_):
    registers[1] = registers[1] ^ registers[2]
    # bitwise XOR of register B and register C into register B. 

def out(operand):
    return combo(operand) % 8
    # combo operand modulo 8, then outputs that value.

def bdv(operand):
    registers[1] = registers[0] // 2 ** combo(operand)
    # adv stored in register B

def bdv_1(operand):
    registers[1] = registers[1] * 2 ** combo(operand)

def cdv(operand):
    registers[2] = registers[0] // 2 ** combo(operand)
    # adv stored in register C

def cdv_1(operand):
    registers[2] = registers[2] * 2 ** combo(operand)

OPS = { 0 : adv, 1 : bxl, 2 : bst, 3 : jnz, 4 : bxc, 5 : out, 6 : bdv, 7 : cdv }

def compute(n, reste):
    adv_1(3, reste)
    return out(4)

i = len(instructions)
while i >= 0:
    n = 0
    i -= 1
    print(instructions[i])
    while compute(n, instructions[i]) != instructions[i]:
        print('yo')
        n += 1
    print(registers)











    # adv_1(3)
    # bxl(6)
    # bxc(3)
    # cdv_1(5)
    # bxl(5)
    # bst_1(4, n)
#    print("-----------------")
