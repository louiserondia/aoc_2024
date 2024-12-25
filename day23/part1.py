from collections import defaultdict
from itertools import combinations

with open('input.txt') as f:
    data = f.read().splitlines()
    data = list(map(lambda l: tuple(l.split('-')), data))

    cache = defaultdict(list)
    for (l, r) in data:
        cache[l] += [r]
        cache[r] += [l]

    res = set()
    for k, v in cache.items():
        comb = tuple(combinations(v, 2))
        for c in comb:
            if c[1] in cache[c[0]]:
                res.add(tuple(sorted((k, c[0], c[1]))))
    res = list(filter(lambda r: any(e.startswith('t') for e in r), res))
    print(len(res))