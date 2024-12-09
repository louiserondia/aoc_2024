with open("input.txt") as f:
    data = list(map(int, f.read()))
    array = []
    for i, e in enumerate(data):
        array.extend([i // 2] * e if not i % 2 else [-1] * e)

    for i, e in enumerate(array):
        if e == -1:
            while array[-1] == -1: array.pop()
            array[i] = array.pop()

    print(sum(i * e for i, e in enumerate(array)))
