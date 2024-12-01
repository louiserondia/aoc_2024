f = list(map(int, open("input.txt", "r").read().split()))

t1 = sorted(f[::2])
t2 = sorted(f[1::2])

s = sum(abs(t1[i] - t2[i]) for i in range(len(t1)))

print(s)
