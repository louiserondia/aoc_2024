import numpy as np

def print_tab(pos):
    tab = '\n'.join(''.join('#' if complex(x, y) in pos else '.' for x in range(w)) for y in range(h))
    print(tab, '\n')

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

    def compute():
        seconds = 0
        prev = 0
        while ~0:
            seconds += 1
            for n in range(len(data)):
                pos[n] = move(speeds[n], pos[n])

            p = np.array(pos)
            indices = np.random.choice(len(p), size=(50, 2))
            d = [abs(p[i] - p[j]) for i, j in indices]
            m = np.mean(d)
            if m < prev or not prev:
                prev = m
                print_tab(pos)
                print(seconds)

    compute()
