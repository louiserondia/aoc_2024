from collections import deque 
from itertools import product

def dijkstra(data):
    open_set = deque([(0, complex(0, 0))])
    closed_set = set([complex(0, 0)])

    while open_set:
        score, target = open_set.popleft()

        if target == complex(70, 70):
            return score

        for d in [1j, -1j, 1, -1]:
            if target + d not in closed_set and target + d in data and data[target + d] != '#':
                open_set.append((score + 1, target + d))
                closed_set.add(target + d)

with open('input.txt') as f:
    data = f.read().split('\n')[:1024]
    data = { complex(int(l.split(',')[0]), int(l.split(',')[1])) : '#' for l in data }
    for i in product(range(71), range(71), repeat=2):
        i = complex(i[0], i[1])
        if i not in data: data[i] = ('.')
    s = dijkstra(data)
    print(s)
    # print(data)