
s = open("input.txt", "r").read()

def v(s):
    if not s.find("mul") and s[3] == "(":
        i = 0
        while s[i + 4].isdigit():
            i += 1
        if i in range(1, 4) and s[i + 4] == ",":
            j = 0
            while s[j + i + 5].isdigit():
                j += 1
            if j in range(1, 4) and s[j + i + 5] == ")":
                return map(int, s[4 : i + j + 5].split(","))

def do(d, s):
    if not s.find("do()"):
        return True
    elif not s.find("don't()"):
        return False
    return d

r = 0
d = True
for i, l in enumerate(s):
    if l == "d":
        d = do(d, s[i : i + 7])
    if l == "m" and v(s[i : i + 13]) and d:
        e1, e2 = v(s[i : i + 12])
        r += e1 * e2

print(r)