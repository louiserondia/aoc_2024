from collections import deque
from itertools import count

def dijkstra(start, score, max_score, data, closed_set):
    open_set = deque([(score, start)])
    cheat = 1

    while open_set and score <= max_score:
        score, target = open_set.popleft()
        if data[target] == 'E':
            return score

        if target in closed_set and closed_set[target] < score:
            continue
        closed_set[target] = score

        for d in [1j, -1j, 1, -1]:
            if target + d in data and (data[target + d] != '#' or cheat > 0):
                if data[target + d] == '#': cheat -= 1
                open_set.append((score + 1, target + d))

def traverse(data):
    cache = {}
    res = []
    def get_path():
        path = []
        p = next(k for k, v in data.items() if v =='S')
        d = 1
        max_score = 0
        while data[p] != 'E':
            cache[p] = max_score
            path.append(p)
            if data[p + d] == '#':
                d = d * 1j if data[p + d * 1j] != '#' else d * -1j
            p += d
            max_score += 1
        return max_score, path
    
    max_score, path = get_path()
    for p in path:
        for nd in [1j, -1j, 1, -1]:
            if p + nd in data and data[p + nd] == '#' and p + nd not in res:
                cheat = dijkstra(p + nd, cache[p] + 1, max_score, data, cache)
                if cheat is not None:
                   res.append(cheat)
    return max_score, res

with open('input.txt') as f:
    data = f.read().splitlines()
    data = { complex(x, y) : e for y, row in enumerate(data) for x, e in enumerate(row) }

    score, res = traverse(data)
    c = count()
    print(res)
    for r in res:
        # if score - r >= 0:
            next(c)
    print(c)