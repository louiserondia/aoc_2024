from functools import reduce
from itertools import combinations

data = list(map(lambda x: list(map(int, x.split())), open("input.txt", "r").read().split("\n")))

def v(l): 
    return  all(i < j and j - i <= 3 for i, j in zip(l, l[1:])) or \
            all(i > j and i - j <= 3 for i, j in zip(l, l[1:]))

def f(acc, l):
    if v(l) or any(v(c) for c in combinations(l, len(l) - 1)):
        return acc + 1
    return acc

r = reduce(f, data, 0)
print(r)