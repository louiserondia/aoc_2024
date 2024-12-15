DIRS = { '>' : 1, 'v' : 1j, '<' : -1, '^' : -1j }

def move(robot, d):
    box = 1
    while coord[robot + d * box] ==  'O':
        box += 1
    if coord[robot + d * box] != '#':
        if box != 1:
            coord[robot + d], coord[robot + d * box] = coord[robot + d * box], coord[robot + d]
        robot += d
    return robot

with open("input.txt") as f:
    coord, dirs = f.read().split('\n\n')
    coord = {complex(x, y): e for y, row in enumerate(coord.split()) for x, e in enumerate(row)}
    dirs = dirs.replace('\n', '')

    robot = next(k for k, v in coord.items() if v == "@")
    for d in dirs:
        robot = move(robot, DIRS[d])

    print(sum(k.real + k.imag * 100 for k, v in coord.items() if v == 'O'))