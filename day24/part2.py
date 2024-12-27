import operator
from itertools import combinations
import heapq

def heuristic(n, t):
    wrong_int = int(n, 2)
    good_int = int(t, 2)

    xor_result = wrong_int ^ good_int
    and_result = wrong_int & good_int
    or_result = wrong_int | good_int

    xor_count = bin(xor_result).count('1')
    and_count = bin(and_result).count('1')
    or_count = bin(or_result).count('1')
    # print('xor_count :', xor_count, 'and_count :', and_count, 'or_count :', or_count,)
    return sum((xor_count, and_count, or_count))


OPS = {'XOR': operator.xor, 'OR': operator.or_, 'AND': operator.and_}

def routine(instructions, info):
    is_success = True
    while instructions:
        executed = set()
        for instru in instructions:
            if instru[0] in info and instru[2] in info: 
                info[instru[3]] = OPS[instru[1]](info[instru[0]], info[instru[2]])
                executed.add(instru)
        if not executed:
            is_success = False
            break
        instructions.difference_update(executed)

    info = reversed([str(info[k]) for k in sorted(info) if k.startswith('z')])
    return is_success, ''.join(info)

def parsing():
    with open('input.txt') as f:
        info, instructions = f.read().split('\n\n')
        info = { line.split(': ')[0]: int(line.split(': ')[1]) for line in info.splitlines() }
        instructions = set(tuple(line.replace('->', '').split()) for line in instructions.splitlines())

        is_success, res = routine(instructions.copy(), info.copy())
        print(is_success, int(res, 2))


        outputs = set()
        for (_, _, _, o) in instructions:
            outputs.add(o)

        x = ''.join(reversed([str(info[k]) for k in sorted(info) if k.startswith('x')]))
        y = ''.join(reversed([str(info[k]) for k in sorted(info) if k.startswith('y')]))    
        target = bin(int(x, 2) + int(y, 2))[2:]
        print('wrong -> ', res)
        print('right -> ', target)
        print('x -> ', int(x, 2))
        print('y -> ', int(y, 2))
        print('total -> ', int(x, 2) + int(y, 2))
        s = sorted(['hcc', 'dtf', 'cjh', 'qmn', 'rck', 'qfs', 'z24', 'dfm'])
        print(','.join(s))
        original_h = heuristic(res, target)

        heap = []
        for comb in combinations(instructions, 2):
            new_instru = set(instructions)
            new_instru.remove(comb[0])
            new_instru.remove(comb[1])
            new_instru.add(tuple(list(comb[0][:-1]) + [comb[1][-1]]))
            new_instru.add(tuple(list(comb[1][:-1]) + [comb[0][-1]]))

            is_succes, res = routine(new_instru, info.copy())
            if is_succes:
                s = heuristic(res, target)
                if s < original_h :
                  heapq.heappush(heap, (s, comb))

        print(len(heap))

        j = 0
        cache = set()
        for comb in combinations(heap, 2):
            j += 1
            all_wires = []
            new_instru = set(instructions)
            
            for c in comb:
                c0 = c[1][0]
                c1 = c[1][1]
                if c0[-1] in all_wires or c1[-1] in all_wires:
                    break
                all_wires.append(c0[-1])
                all_wires.append(c1[-1])
                new_instru.remove(c0)
                new_instru.remove(c1)
                new_instru.add(tuple(list(c0[:-1]) + [c1[-1]]))
                new_instru.add(tuple(list(c1[:-1]) + [c0[-1]]))
            if len(all_wires) != 4:
                continue
            is_succes, res = routine(new_instru, info.copy())
            if is_succes: 
                # print('res', res, '--> ', j)
                if res == target:
                    # print('YOOOOO', all_wires, ' <------- \n', comb)
                    cache.add(tuple(all_wires))

        print(cache)
        print(len(cache))
parsing()