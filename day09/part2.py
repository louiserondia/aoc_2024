def find_first_spot(array, size):
    s = 0
    for i, e in enumerate(array):
        if e == -1: s += 1
        else: s = 0
        if s == size: return i - size + 1
    return -1

with open("input.txt") as f:
    data = list(map(int, f.read()))
    array = []
    for i, e in enumerate(data):
        array.extend([i // 2] * e if not i % 2 else [-1] * e)

    size = 0
    old_e = array[-1]
    for i, e in enumerate(array[::-1]):
        if e == old_e:
            size += 1
        elif old_e != -1:
            index = find_first_spot(array[:len(array) - i:], size)
            if index != -1:
                for j in range(size):
                    array[len(array) - i + j], array[index + j] = -1, old_e
        if e != old_e:
            size = 1
        old_e = e

    print(sum(i * e for i, e in enumerate(array) if e != -1))
