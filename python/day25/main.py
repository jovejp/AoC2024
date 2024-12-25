from collections import defaultdict

filename = "input.txt"
# filename = "sample.txt"

with open(filename) as file:
    content = file.read()

g = [[[item.strip() for item in line.strip()] for line in block.split('\n')] for block in content.split('\n\n')]

# print(g)
gn = len(g)
row = len(g[0])
col = len(g[0][0])
# print(gn, row, col)

keys = defaultdict(list)
locks = defaultdict(list)


def print_grid(tg):
    for i in range(row):
        print("".join(tg[i]))


def simc_keys():
    base_key = defaultdict(int)
    for kg in range(gn):
        key = base_key.copy()
        dg = g[kg]
        # print_grid(dg)
        for i in range(row):
            for j in range(col):
                if dg[i][j] == '#':
                    key[j] += 1
        if dg[0][0] == '#':
            keys[kg] = [value for _, value in sorted(key.items())]
        elif dg[row - 1][0] == '#':
            locks[kg] = [value for _, value in sorted(key.items())]
        # print(key)


simc_keys()
# print(keys)
# print(locks)


def check_key_lock(arr1, arr2):
    for x, y in zip(arr1, arr2):
        if x + y > row:
            return False
    return True


def part1():
    total_match = 0
    visited = []
    for key in keys:
        for lock in locks:
            if check_key_lock(keys[key], locks[lock]):
                # print("Matched")
                # print(keys[key], locks[lock])
                total_match += 1
                # if locks[lock] not in visited:
                #     total_match += 1
                #     visited.append(locks[lock])
                # if keys[key] not in visited:
                #     total_match += 1
                #     visited.append(keys[key])

    return total_match


def part2():
    return 0


print("Part one:", part1())
print("Part two:", part2())
