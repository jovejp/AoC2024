from collections import defaultdict, deque
import math
import re

filename = "input.txt"
# filename = "sample.txt"
with open(filename) as file:
    content = file.read()

part1, part2 = content.split('\n\n', 1)

g1 = [[item.strip() for item in line.strip().split(':')] for line in part1.split('\n')]
# print(g1)

base_cached_dict = defaultdict(int)

for item in g1:
    if item[0] not in base_cached_dict:
        base_cached_dict[item[0]] = int(item[1])

g2 = [[item.strip() for item in re.split(r'\s+|->', line) if item.strip()] for line in part2.split('\n')]


# print(g2)


def simc_compute(d, cached_dict):
    queue = deque()
    seen = set()
    for item in d:
        queue.append((item[-1], item[:-1]))

    while queue:
        key, operations = queue.popleft()
        if key in cached_dict:
            continue
        x, op, y = operations
        # print(x, op, y)
        if x in cached_dict and y in cached_dict:
            if op == 'AND':
                cached_dict[key] = cached_dict[x] & cached_dict[y]
            elif op == 'OR':
                cached_dict[key] = cached_dict[x] | cached_dict[y]
            elif op == 'XOR':
                cached_dict[key] = cached_dict[x] ^ cached_dict[y]
            else:
                print("error!!!", x, op, y)
        else:
            queue.append((key, operations))


base_result_part1 = []


def part1():
    bin_number = ''
    cached_dict = base_cached_dict.copy()
    simc_compute(g2.copy(), cached_dict)
    # print(cached_dict)
    z_keys = sorted([key for key in cached_dict.keys() if key.startswith('z')], reverse=True)
    for z_key in z_keys:
        # print(z_key, cached_dict[z_key])
        bin_number += str(cached_dict[z_key])
    base_result_part1.append(int(bin_number, 2))
    return base_result_part1[-1]


full_gates = set()
cached_gates = defaultdict(set)


def cache_gates():
    for item in g2:
        if item[-1] not in full_gates:
            full_gates.add(item[-1])
        if item[0] not in cached_gates[item[-1]]:
            cached_gates[item[-1]].add(item[0])
            cached_gates[item[-1]].add(item[2])
    # print("cached_gates", cached_gates)


cache_gates()


def cache_z_gates():
    for s in cached_gates:
        # if s.startswith('z'):
        queue = deque()
        for ss in cached_gates[s]:
            queue.append(ss)
        while queue:
            ss = queue.popleft()
            if ss not in cached_gates:
                continue
            else:
                for sss in cached_gates[ss]:
                    if sss not in cached_gates[s]:
                        cached_gates[s].add(sss)
                        queue.append(sss)
    # print("cache_z_gates", cached_gates)


cache_z_gates()


def get_simc_value(nf, nd):
    bin_number = ''
    simc_compute(nf, nd)
    # print(nd)
    z_keys = sorted([key for key in nd.keys() if key.startswith('z')], reverse=True)

    for z_key in z_keys:
        # print(z_key, cached_dict[z_key])
        bin_number += str(nd[z_key])
    return int(bin_number, 2)


def find_bad_gates(nf, cost, potential_list=None):
    if potential_list is None:
        potential_list = []
    base_nd = base_cached_dict.copy()
    count_errors = 0
    for item in base_nd:
        base_nd[item] = 0
    for i in range(45):
        item_x = 'x' + str(i).zfill(2)
        item_y = 'y' + str(i).zfill(2)
        item_z = 'z' + str(i).zfill(2)
        for j in [0, 1]:
            for k in [0, 1]:
                if j == 0 and k == 0:
                    compare_data = 0
                elif j == 1 and k == 1:
                    compare_data = 2 ** (i + 1)
                else:
                    compare_data = 2 ** i
                nd = base_nd.copy()
                nd[item_x] = j
                nd[item_y] = k
                result = get_simc_value(nf, nd)
                if result != compare_data:
                    # print("error", item_x, item_y, item_z, i, j, k, result, compare_data)
                    if item_z not in potential_list:
                        potential_list.append(item_z)
                    count_errors += 1
                if count_errors > cost:
                    return count_errors
    return count_errors


def part2():
    nf = g2.copy()
    potential_list = []
    cost = find_bad_gates(nf, 100, potential_list)
    print("cost", cost)
    print("potential_list", potential_list)
    potential_list.append('nbd')  # find from full loop

    finds = defaultdict(int)
    finds_switched = defaultdict(str)

    seen = set()
    for i in range(0, len(nf)):
        if nf[i][-1] == 'z00':
            continue
        if nf[i][-1] not in potential_list:
            continue
        for j in range(0, len(nf)):
            if nf[j][-1] == 'z00' or nf[i][-1] == nf[j][-1]:
                continue
            if nf[i][-1] in cached_gates[nf[j][-1]] or nf[j][-1] in cached_gates[nf[i][-1]]:
                continue
            if frozenset((nf[i][-1], nf[j][-1])) in seen:
                continue
            else:
                seen.add(frozenset((nf[i][-1], nf[j][-1])))
                pni = nf[i].copy()
                pni[-1] = nf[j][-1]
                pnj = nf[j].copy()
                pnj[-1] = nf[i][-1]
                nnf = nf.copy()
                nnf[i] = pnj
                nnf[j] = pni
                new_cost = find_bad_gates(nnf, cost)
                if new_cost < cost:
                    if new_cost < finds.get(nf[i][-1], float("inf")):
                        print("new_cost", new_cost)
                        print("switched", nf[j][-1], nf[i][-1])
                        finds[nf[i][-1]] = new_cost
                        finds_switched[nf[i][-1]] = nf[j][-1]
                        # cost = new_cost
                        # nnnf = nnf.copy()
    print(finds_switched)
    smallest_keys = sorted(finds, key=finds.get)[:4]
    return ','.join(sorted(smallest_keys + [finds_switched[key] for key in smallest_keys]))


print("Part one:", part1())
print("Part two:", part2())
