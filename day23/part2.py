from collections import defaultdict
from itertools import combinations

def is_clique(nodes, graph):
    return not any(b not in graph[a] for a in nodes for b in nodes if a != b)

with open('input.txt') as f:
    data = f.read().splitlines()
    data = list(map(lambda l: tuple(l.split('-')), data))

    cache = defaultdict(list)
    for (l, r) in data:
        cache[l] += [r]
        cache[r] += [l]

    def find_biggest_clique():
        keys = list(cache.keys())
        for size in range(len(keys) - 1):
            comb = combinations(keys, size)
            for subset in comb:
                if (is_clique(subset, cache)):
                    print(sorted(subset))
                    break
    
    find_biggest_clique()
