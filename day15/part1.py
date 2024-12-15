DIRS = { '>' : 1, 'v' : 1j, '<' : -1, '^' : -1j }

with open("input.txt") as f:
    coord, dirs = f.read().split('\n\n')
    coord = {complex(x, y): e for y, row in enumerate(coord.split()) for x, e in enumerate(row) if e != '.'}
    dirs = dirs.replace('\n', '')

    def move(robot, d):
        box = 1
        while robot + d * box in coord and coord[robot + d * box] ==  'O':
            box += 1
        if robot + d * box not in coord or coord[robot + d * box] != '#':
            if box != 1:
                coord.pop(robot + d)
                coord[robot + d * box] = 'O'
            robot += d
        return robot
    
    for k, v in coord.items():
        if v == "@": robot = k
    coord.pop(k)

    for d in dirs:
        robot = move(robot, DIRS[d])

    s = sum(k.real + k.imag * 100 for k, v in coord.items() if v == 'O')
 
    print(s)