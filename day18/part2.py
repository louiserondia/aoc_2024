DIRS = [1j, -1j, 1, -1]

def traverse(data):
    parents = {}
    for k, v in data.items():
        if v == '.':
            if k not in parents:
                parents[k] = k
            def add(k):
                for d in DIRS:
                    if k + d in data and data[k + d] == '.' and k + d not in parents:
                        parents[k + d] = k
                        add(k + d)
            add(k)
    return parents

def add_parent(pos, parents, data):
    parents[pos] = pos
    for d in DIRS:
        if pos + d in data and data[pos + d] != '#':
            union(pos, pos + d, parents)

def find(x, parents):
    return find(parents[x], parents) if parents[x] != x else x

def union(x, y, parents):
    parents[find(y, parents)] = find(x, parents)

with open('input.txt') as f:
    data = f.read().splitlines()
    byte = [ complex(int(x), int(y)) for l in data for x, y in [l.split(',')]]
    data = { complex(x, y): '#' if complex(x, y) in byte else '.' for y in range(71) for x in range(71) }

    parents = traverse(data)
    for b in byte[::-1]:
        data[b] = '.'
        add_parent(b, parents, data)
        if find(complex(0, 0), parents) == find(complex(70, 70), parents):
            print(b)
            break
