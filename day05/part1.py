from collections import defaultdict

def v(pages, conditions):
    for i, n in enumerate(pages):
        if n in conditions and any(c in conditions[n] for c in pages[i:]):
            return 0
    return int(pages[(len(pages) - 1) // 2])

with open("input.txt", "r") as f:
    cond, lists = f.read().split("\n\n")
    cond = list(map(lambda l: tuple(l.split("|")), cond.split("\n")))
    lists = list(map(lambda l: l.split(","), lists.split("\n")))

    conditions = defaultdict(list)
    for (val, key) in cond: conditions[key].append(val)

    print(sum(v(l, conditions) for l in lists))