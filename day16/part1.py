import heapq
import itertools
c = itertools.count()

def dijkstra(start, end):
    open_set = [(0, next(c), start, 1, 0)]
    closed_set = {}

    while open_set:
        score, _, tile, d, prev = heapq.heappop(open_set)
        if tile == end:
            return score
        if tile in closed_set:
            continue
        closed_set[tile] = (score, prev)

        for n in range(4):
            nd, ns = d * 1j ** n, score + 1 + (1000 if n else 0)
            if data[tile + nd] == '#' or (tile + nd in closed_set and closed_set[tile + nd][0] <= ns):
                continue
            heapq.heappush(open_set, (ns, next(c), tile + nd, nd, tile))

with open('input.txt') as f:
    data = { complex(x, y): e for y, row in enumerate(f.read().split()) for x, e in enumerate(row) }
    start, end = next(k for k, v in data.items() if v == 'S'), next(k for k, v in data.items() if v == 'E')

    print(dijkstra(start, end))
