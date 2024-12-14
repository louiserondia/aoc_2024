from functools import reduce

def parse(line):
    p, v = line.split()
    px, py = list(map(int, p[2:].split(',')))
    vx, vy = list(map(int, v[2:].split(',')))
    return complex(px, py), complex(vx, vy)

with open('input.txt') as f:
    data = list(map(lambda line: parse(line), f.read().split('\n')))
    speeds = [line[1] for line in data]
    pos = [line[0] for line in data]

    w, h = 101, 103

    def move(v, p): return complex((p.real + v.real) % w, (p.imag + v.imag) % h)

    for _ in range(100):
        for i in range(len(data)):
            pos[i] = move(speeds[i], pos[i])
    
    tab = [0] * 4
    for n in range(len(data)):
        x, y = pos[n].real / (w // 2), pos[n].imag / (h // 2)
        if x != 1 and y != 1: 
            i = (x > 1) + 2 * (y > 1)
            tab[i] += 1
    print(reduce(lambda x, y: x * y, tab))

