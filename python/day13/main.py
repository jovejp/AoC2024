import re, math

filename = "input.txt"
# filename = "sample.txt"
groups = []

with open(filename, 'r') as file:
    lines = file.readlines()
    current_group = {}
    for line in lines:
        line = line.strip()
        if not line:
            if current_group:
                groups.append(current_group)
                current_group = {}
            continue

        match = re.match(r'Button (\w): X\+(\d+), Y\+(\d+)', line)
        if match:
            button, x, y = match.groups()
            current_group[button] = (int(x), int(y))
        else:
            match = re.match(r'Prize: X=(\d+), Y=(\d+)', line)
            if match:
                x, y = match.groups()
                current_group['P'] = (int(x), int(y))
    if current_group:
        groups.append(current_group)


def simc(group):
    a0, a1 = group['A']
    b0, b1 = group['B']
    p0, p1 = group['P']
    result = {}
    i = 1
    while i < p0 // a0 and i <= 100:
        if (p0 - i * a0) % b0 == 0:
            j = (p0 - i * a0) / b0
            if p1 == i * a1 + j * b1 and j <= 100:
                result[(int(i), int(j))] = int(3 * i + j)
        i += 1
    return result


def part1():
    total = 0
    for group in groups:
        result = simc(group)
        if result:
            # print(result)
            min_item = min(result.items(), key=lambda x: x[1])
            total += min_item[1]
            # print(min_item[1])
    return total


def simc2(group):
    # matrix-inverse
    # reference here for matrix inverse => https://www.shuxuele.com/algebra/matrix-inverse.html
    result = {}
    a0, a1 = group['A']
    b0, b1 = group['B']
    p0, p1 = group['P']
    p0 += 10000000000000
    p1 += 10000000000000
    det = (a0 * b1 - a1 * b0)
    i = int(round((b1 * p0 - b0 * p1)/det))
    j = int(round((a0 * p1 - a1 * p0)/det))
    # print(det, i, j)

    if i * a0 + b0 * j == p0 and i * a1 + b1 * j == p1:
        result[(int(i), int(j))] = int(3 * i + j)
        # print("result", result)
    return result


def part2():
    total = 0
    for group in groups:
        result = simc2(group)
        if result:
            min_item = min(result.items(), key=lambda x: x[1])
            total += min_item[1]
    return total


print("Part one:", part1())
print("Part two:", part2())
