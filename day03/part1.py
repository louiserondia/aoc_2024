
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
                return map(int, s[4 : j + i + 5].split(","))
            
r = 0
for i, l in enumerate(s):
    if l == "m" and v(s[i : i + 13]):
        e1, e2 = v(s[i : i + 12])
        r += e1 * e2

print(r)