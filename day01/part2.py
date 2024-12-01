from collections import Counter

f = list(map(int, open("input.txt", "r").read().split()))

t1 = sorted(f[::2])
t2 = sorted(f[1::2])

c = Counter(t2)

s = sum(v * c.get(v, 0) for v in t1)
print(s)
