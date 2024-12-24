
def routine(n):
    n = (n ^ n * 64) % 16777216
    n = (n ^ n // 32) % 16777216
    n = (n ^ n * 2048) % 16777216
    return n

with open('input.txt') as f:
    data = list(map(int, f.read().splitlines()))

    seq = (None,) * 4
    cache = {}
    for i, n in enumerate(data):
        prev = None
        saleman = n
        for _ in range(2000):
            n = routine(n)
            if prev is not None:
                seq = seq[1:] + (((n % 10) - prev),)
            if not any(e is None for e in seq):
                if seq in cache:
                    if any(s == saleman for s, _ in cache[seq]):
                        prev = n % 10
                        continue
                    cache[seq] = cache[seq] + ((saleman, n % 10),)
                elif seq not in cache: cache[seq] = ((saleman, n % 10),)
            prev = n % 10
        print(i)
    
    for key, val in cache.items():
        cache[key] = sum(v[1] for v in val)

    res = max(cache, key=cache.get )
    print(res)
    print(cache[res])
