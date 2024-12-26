from collections import defaultdict

with open('input.txt') as f:
    edges = f.read().splitlines()
    edges = list(map(lambda l: tuple(l.split('-')), edges))

    neighbours = defaultdict(list)
    for (l, r) in edges:
        neighbours[l] += [r]
        neighbours[r] += [l]

    vertices = list(neighbours.keys())

    res = []
    def bk(r, p, x):
        global res
        if not bool(p) and not bool(x):
            if len(r) > len(res):
                res = r
            return
        pivot = (p + x)[0]
        for v in filter(lambda e: e not in neighbours[pivot], p):
            next_p = list(filter(lambda n: n in p, neighbours[v]))
            next_x = list(filter(lambda n: n in x, neighbours[v]))
            bk(r + [v], next_p, next_x)
            p.remove(v)
            x.append(v)

    bk([], vertices, [])
    print(','.join(sorted(res)))