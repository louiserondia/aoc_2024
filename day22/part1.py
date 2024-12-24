with open('input.txt') as f:
    data = list(map(int, f.read().splitlines()))

    s = 0
    for n in data:
        for _ in range(2000):
            n = (n ^ n * 64) % 16777216
            n = (n ^ n // 32) % 16777216
            n = (n ^ n * 2048) % 16777216
        s += n
    print(s)
