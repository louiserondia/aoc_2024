DIRS = [-1 - 1j, 1 - 1j, 1 + 1j, -1 + 1j]

def look_around(coord, grid):
    s = "".join(grid.get(coord + d, 'O') for d in DIRS)
    return s in {"MMSS", "SMMS", "SSMM", "MSSM"}

with open("input.txt", "r") as f:
    data = f.read().split('\n')
    grid = {complex(x, y): e for y, row in enumerate(data) for x, e in enumerate(row)}
    r = sum(look_around(z, grid) for z, e in grid.items() if e == "A")

    print (r)