
s = open("input.txt", "r").read()

def v(s):
    if s.find("mul") == 0 and s[3] == "(":
        i = 0
        while s[i + 4].isdigit():
            i += 1
        if i in range(1, 4) and s[i + 4] == ",":
            j = 0
            while s[j + i + 4 + 1].isdigit():
                j += 1
            if j in range(1, 4) and s[j + i + 4 + 1] == ")":
                return s[4:4+i+1+j]       
            
r = 0
for i, l in enumerate(s):
    if l == "m" and v(s[i:i+13]):
        e1, e2 = map(int, v(s[i:i+12]).split(","))
        r += e1 * e2

print(r)