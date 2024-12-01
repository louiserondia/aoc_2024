from collections import Counter

data = list(map(int, open("input.txt", "r").read().split()))

t1 = sorted(data[::2])
t2 = sorted(data[1::2])

c = Counter(t2)

s = sum(v * c.get(v, 0) for v in t1)
print(s)
