dirs = [(-1, -1), (1, -1), (1, 1), (-1, 1)]

def move(c, d):
    return (c[0] + d[0], c[1] + d[1])

def look_around(coord, grid):
    s = ""
    for d in dirs:
        s += grid.get(move(coord, d), grid[coord])
    return s in {"MMSS", "SMMS", "SSMM", "MSSM"}

with open("input.txt", "r") as f:
    data = f.read().split('\n')
    grid = {(x, y): e for y, row in enumerate(data) for x, e in enumerate(row)}

    r = sum(look_around((x, y), grid) for (x, y), e in grid.items() if e == "A")

    print (r)