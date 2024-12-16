import heapq
import itertools
c = itertools.count()

def dijkstra(start, end):
    open_set = [(0, next(c), start, 1, [])]
    closed_set = {}
    paths = set()
    best_score = float('inf')

    while open_set:
        score, _, tile, d, path = heapq.heappop(open_set)
        if tile == end:
            print(score)
            paths = set(path + [tile])
            # print('--->', open_set, '\n\n')
            print('--->', heapq.nsmallest(3, open_set), '\n\n')
            return len(paths)
        if tile not in closed_set:
            closed_set[tile] = (score, path + [tile])


        if data[tile + d] != '#' and tile + d not in closed_set:
            heapq.heappush(open_set, (score + 1, next(c), tile + d, d, path + [tile]))
        for n in [1j, -1j]:
                heapq.heappush(open_set, (score + 1000, next(c), tile, d * n, path))

with open('input.txt') as f:
    data = { complex(x, y): e for y, row in enumerate(f.read().split()) for x, e in enumerate(row) }
    start, end = next(k for k, v in data.items() if v == 'S'), next(k for k, v in data.items() if v == 'E')

    print(dijkstra(start, end))
