from functools import reduce

data = list(map(lambda x: list(map(int, x.split())), open("input.txt", "r").read().split("\n")))

def v(l):
    return  all(i < j and j - i <= 3 for i, j in zip(l, l[1:])) or \
            all(i > j and i - j <= 3 for i, j in zip(l, l[1:]))

r = reduce(lambda acc, l: acc + 1 if v(l) else acc, data, 0)
print(r)