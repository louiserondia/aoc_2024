def parse(line):
    (x, y) = line.split(',')
    x = int(x[x.find('X') + 2:])
    y = int(y[y.find('Y') + 2:])
    return (x, y)

cache = set()

with open("input.txt") as f:
    data = f.read().split('\n\n')
    data = list(map(lambda block: list(map(lambda line: parse(line), block.split('\n'))), data))

    def solve(a, b, dest):
        dest_x, dest_y = dest
        ax, ay = a
        bx, by = b
        score_a, score_b = 0, 0

        score_b = ((dest_x * ay) - (dest_y * ax)) / ((bx * ay) - (by * ax))
        score_a = (dest_y - (score_b * by)) / ay
        return (score_a, score_b)

    r = 0
    for block in data:
        (a, b) = solve(block[0], block[1], block[2])
        if a % 1 == 0 and b % 1 == 0 and a <= 100 and b <= 100:
            r += 3 * a + b
    print(r)