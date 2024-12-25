from collections import defaultdict

def routine(n):
    n = (n ^ n * 64) % 16777216
    n = (n ^ n // 32) % 16777216
    n = (n ^ n * 2048) % 16777216
    return n

with open('input.txt') as f:
    data = list(map(int, f.read().splitlines()))

    sale_cache = {}
    for i, n in enumerate(data):
        seq = (None,) * 4
        prev = n % 10
        cache = {}

        for _ in range(2000):
            n = routine(n)
            current = n % 10

            seq = seq[1:] + (current - prev,)
            if None not in seq and seq not in cache:
                cache[seq] = current
            prev = current
        sale_cache[i] = cache

    merged = defaultdict(int)
    for salesman in sale_cache.values():
        for seq, score in salesman.items():
            merged[seq] += score
    
    r = max(merged, key=merged.get)
    print(merged[r])