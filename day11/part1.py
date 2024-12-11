def solve(e, i):
    if i == 0:
        return 1
    if e == 0:
        return solve(1, i - 1)
    if not len(str(e)) % 2:
        l = len(str(e)) // 2 
        return solve(int(str(e)[l:]), i - 1) + solve(int(str(e)[:l]), i - 1)
    return solve(e * 2024, i - 1)

with open("input.txt") as f:
    data = list(map(int, f.read().split()))
    print(sum(solve(e, 25) for e in data))