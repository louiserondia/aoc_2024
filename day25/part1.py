
def calc(item):
    height = [-1] * 5
    for row in item:
        for x, e in enumerate(row):
            if e == '#': height[x] += 1
    return height

with open('input.txt') as f:
    data = f.read().split('\n\n')
    keys = list(filter(lambda d: d.startswith('.'), data))
    locks = list(filter(lambda d: d.startswith('#'), data))

    res = set()
    for l in locks:
        lh = calc(l.splitlines())
        for k in keys:
            kh = calc(k.splitlines())
            if (all(e[0] + e[1] < 6 for e in zip(lh, kh))):
                res.add((l, k))
    print(len(res))