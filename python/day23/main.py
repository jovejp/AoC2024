from collections import defaultdict, deque
from functools import cache

filename = "input.txt"
# filename = "sample.txt"
with open(filename) as file:
    g = [line.strip().split('-') for line in file.readlines()]

rows, cols = len(g), len(g[0])
print(g)

vn = defaultdict(set)
vp = set()

for i in range(rows):
    if g[i][1] not in vn[g[i][0]]:
        vn[g[i][0]].add(g[i][1])
    if g[i][0] not in vn[g[i][1]]:
        vn[g[i][1]].add(g[i][0])
    if frozenset((g[i][0], g[i][1])) not in vp:
        vp.add(frozenset(g[i]))

print("vn", vn)
print("vp", vp)


def simc_tc():
    three_conn = set()
    for k in vn.keys():
        ll = list(vn[k])
        for r in range(len(ll)):
            for rr in range(r + 1, len(ll)):
                if frozenset((ll[r], ll[rr])) in vp:
                    if any(x.startswith('t') for x in [k,ll[r], ll[rr]]):
                        three_conn.add(frozenset((k, ll[r], ll[rr])))
    return three_conn


def part1():
    tcd = simc_tc()
    print(tcd)
    return len(tcd)


@cache
def simc_2(nodes=frozenset()):
    best = nodes
    for start in vn:
        if start in nodes:
            continue
        if nodes - vn[start]:
            continue
        new = simc_2(nodes | {start})
        if len(new) > len(best):
            best = new
    return best


def part2():
    tcd = simc_2()
    result = (",".join(sorted(tcd)))
    return result


print("Part one:", part1())
print("Part two:", part2())
