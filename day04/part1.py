dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

def move(c, d):
    return (c[0] + d[0], c[1] + d[1])

def look_around(coord, grid):
    r = 0
    for d in dirs:
        n = coord
        s = "".join(grid.get((n := move(n, d)), grid[coord]) for _ in range(3))
        if s == "MAS":
            r += 1
    return r

with open("input.txt", "r") as f:
    data = f.read().split('\n')
    grid = {(x, y): e for y, row in enumerate(data) for x, e in enumerate(row)}

    r = sum(look_around((x, y), grid) for (x, y), e in grid.items() if e == "X")

    print (r)