from collections import defaultdict

def fix(pages, conditions, modified=False):
    while ~0:
        m = False
        for i, n in enumerate(pages):
            for j, c in enumerate(pages[i:]):
                if n in conditions and c in conditions[n]:
                    pages.insert(i + j, pages.pop(i))
                    modified, m = True, True
                    break
        if not m: break
    return (int(pages[(len(pages) - 1) // 2]), modified)

with open("input.txt", "r") as f:
    cond, lines = f.read().split("\n\n")
    cond = list(map(lambda l: tuple(l.split("|")), cond.split("\n")))
    lines = list(map(lambda l: l.split(","), lines.split("\n")))

    conditions = defaultdict(list)
    for (val, key) in cond: conditions[key].append(val)

    print(sum(score for score, modified in (fix(l, conditions) for l in lines) if modified))