DIRS = [1j, 1, -1j, -1, 1 + 1j, -1 - 1j, -1 + 1j, 1 - 1j]

def look_around(coord, grid):
    r = 0
    for d in DIRS:
        n = coord
        s = "".join(grid.get((n := n + d), 'O') for _ in range(3))
        if s == "MAS":
            r += 1
    return r

with open("input.txt", "r") as f:
    data = f.read().split('\n')
    grid = {complex(x, y): e for y, row in enumerate(data) for x, e in enumerate(row)}

    r = sum(look_around(z, grid) for z, e in grid.items() if e == "X")

    print (r)


