from collections import deque
from itertools import count

def dijkstra(start, score, max_score, data):
    open_set = deque([(score, start)])
    closed_set = set([start])

    while open_set and score <= max_score:
        score, target = open_set.popleft()
        if data[target] == 'E':
            return score

        for d in [1j, -1j, 1, -1]:
            if  target + d not in closed_set and target + d in data and \
                (data[target + d] != '#' or (data[target + d] != '#' and not score)):
                    open_set.append((score + 1, target + d))
                    closed_set.add(target + d)

def traverse(data):
    res = {}
    def get_path():
        p = next(k for k, v in data.items() if v =='S')
        d = 1
        max_score = 0
        path = []
        while data[p] != 'E':
            path.append(p)
            if data[p + d] == '#':
                d = d * 1j if data[p + d * 1j] != '#' else d * -1j
            p += d
            max_score += 1
        return max_score, path
    max_score, path = get_path()

    score = 0
    for p in path:
        for nd in [1j, -1j, 1, -1]:
            if p + nd in data and data[p + nd] == '#' and p + nd not in res:
                cheat = dijkstra(p + nd, score + 1, max_score, data)
                if cheat is not None:
                   res[p + nd] = cheat
        score += 1
    return max_score, res

with open('input.txt') as f:
    data = f.read().splitlines()
    data = { complex(x, y) : e for y, row in enumerate(data) for x, e in enumerate(row) }

    score, res = traverse(data)
    c = count()
    for r in res.values():
        if score - r >= 100:
            next(c)
    print(c)