from collections import defaultdict
DIRS = { '>' : 1, 'v' : 1j, '<' : -1, '^' : -1j }

with open("input.txt") as f:
    coord, dirs = f.read().split('\n\n')
    coord = coord.replace('#', '##')
    coord = coord.replace('O', '[]')
    coord = coord.replace('.', '..')
    coord = coord.replace('@', '@.')
    w, h = len(coord.split()[0]), len(coord.split())
    coord = {complex(x, y): e for y, row in enumerate(coord.split()) for x, e in enumerate(row) if e != '.'}
    dirs = dirs.replace('\n', '')
    cache = defaultdict(list)

    def boxes_involved(box, d, level):
        if box not in coord:
            return True
        if coord[box] == '#':
            return False
        if box not in cache[level]:
            cache[level].append(box)
        if coord[box] == ']':
            if box - 1 not in cache[level]:
                cache[level].append(box - 1)
            return boxes_involved(box + d - 1, d, level + 1) and boxes_involved(box + d, d, level + 1)
        if coord[box] == '[':
            if box + 1 not in cache[level]:
                cache[level].append(box + 1)
            return boxes_involved(box + d + 1, d, level + 1) and boxes_involved(box + d, d, level + 1)
        return True

    def move(robot, d):
        if (d == 1j or d == -1j) and robot + d in coord and coord[robot + d] in '[]':
            if boxes_involved(robot + d, d, 0):
                m = max(cache.keys())
                for level in range(m, -1, -1):
                    for c in cache[level]:
                        coord[c + d] = coord.pop(c)
                robot += d
            cache.clear()
            return robot
        
        box = 1
        while robot + d * box in coord and coord[robot + d * box] in '[]':
            box += 1
        if robot + d * box not in coord or coord[robot + d * box] != '#':
            while box > 1:
                coord[robot + d * box] = coord.pop(robot + d * (box - 1))
                box -= 1
            robot += d
        return robot
    
    for k, v in coord.items():
        if v == "@": robot = k

    for d in dirs:
        robot = move(robot, DIRS[d])

    print(sum(k.real + k.imag * 100 for k, v in coord.items() if v == '['))