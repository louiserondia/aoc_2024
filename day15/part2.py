from collections import defaultdict

DIRS = { '>' : 1, 'v' : 1j, '<' : -1, '^' : -1j }
cache = defaultdict(list)

def pyramid(box, d, level):
    if coord[box] == '.':
        return True
    if coord[box] == '#':
        return False

    offset = -1 if coord[box] == ']' else 1

    for b in (box, box + offset):
        if b not in cache[level]: cache[level].append(b)
    return pyramid(box + d + offset, d, level + 1) and pyramid(box + d, d, level + 1)

def move(robot, d):
    if d in (1j, -1j) and coord[robot + d] in '[]':
        if pyramid(robot + d, d, 0):
            for level in reversed(cache.keys()):
                for c in cache[level]:
                    coord[c + d], coord[c] = coord[c], coord[c + d]
            robot += d
        cache.clear()
        return robot
    
    box = 1
    while coord[robot + d * box] in '[]':
        box += 1
    if coord[robot + d * box] != '#':
        while box > 1:
            coord[robot + d * box], coord[robot + d * (box - 1)] = coord[robot + d * (box - 1)], coord[robot + d * box]
            box -= 1
        robot += d
    return robot

with open("input.txt") as f:
    coord, dirs = f.read().split('\n\n')
    coord = coord.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.')
    coord = { complex(x, y): e for y, row in enumerate(coord.split()) for x, e in enumerate(row)}
    dirs = dirs.replace('\n', '')

    robot = next(k for k, v in coord.items() if v == "@")
    for d in dirs:
        robot = move(robot, DIRS[d])

    print(sum(k.real + k.imag * 100 for k, v in coord.items() if v == '['))