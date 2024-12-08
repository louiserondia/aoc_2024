def solve(s, elements, score):
    if len(elements) == 0 and score == s:
        return score
    elif len(elements) == 0 or score > s:
        return 0
    return max(solve(s, elements[1:], score + elements[0]),
               solve(s, elements[1:], score * elements[0]),
               solve(s, elements[1:], int(str(score) + str(elements[0]))))

with open("input.txt", 'r') as f:
    data = map(lambda l: l.split(':'), f.read().split('\n'))
    data = map(lambda pair: (int(pair[0]), list(map(int, pair[1].split()))), data)

    print(sum(solve(s, e[1:], e[0]) for (s, e) in data))

