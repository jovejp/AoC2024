import re

filename = "input.txt"
# filename = "sample.txt"

with open(filename) as file:
    content = file.read()

# Use regular expressions to find the values
RA = int(re.search(r'Register A: (\d+)', content).group(1))
RB = int(re.search(r'Register B: (\d+)', content).group(1))
RC = int(re.search(r'Register C: (\d+)', content).group(1))
PG = list(map(int, re.search(r'Program: ([\d,]+)', content).group(1).split(',')))


def run_part1(a, b, c):
    i, out = 0, []
    while i in range(len(PG) - 1):
        # print("i", i, "A:", a, a % 8, "B:", b, "C:", c, "out:", out)
        opm = {0: 0, 1: 1, 2: 2, 3: 3, 4: a, 5: b, 6: c}
        op, opv = PG[i], PG[i + 1]
        match op:
            case 0:
                a = a // 2 ** opm[opv]
            case 1:
                b = b ^ opv
            case 2:
                b = opm[opv] % 8
            case 3:
                if a != 0:
                    i = opv - 2
            case 4:
                b = b ^ c
            case 5:
                out = out + [opm[opv] % 8]
            case 6:
                b = a // 2 ** opm[opv]
            case 7:
                c = a // 2 ** opm[opv]
            case _:
                print("Error!!!!!!! Invalid opt value", op)
        i += 2

    return out


def part1():
    return run_part1(RA, RB, RC)


part2_result = []


def run_part2(position, r):
    if position < 0:
        part2_result.append(r)
        return True
    for guess in range(8):
        a = r * 8 + guess
        i, b, c = 0, 0, 0
        out = -1
        while i in range(len(PG) - 1):
            opm = {0: 0, 1: 1, 2: 2, 3: 3, 4: a, 5: b, 6: c}
            op, opv = PG[i], PG[i + 1]
            match op:
                case 0:
                    a = a // 2 ** opm[opv]
                case 1:
                    b = b ^ opv
                case 2:
                    b = opm[opv] % 8
                case 3:
                    if a != 0:
                        i = opv - 2
                case 4:
                    b = b ^ c
                case 5:
                    out = opm[opv] % 8
                    break
                case 6:
                    b = a // 2 ** opm[opv]
                case 7:
                    c = a // 2 ** opm[opv]
                case _:
                    print("Error!!!!!!! Invalid opt value", op)
            i += 2
        if out == PG[position] and run_part2(position - 1, r * 8 + guess):
            return True
    return False


def part2():
    run_part2(len(PG) - 1, 0)
    return part2_result[0]


print("Part one:", part1())
print("Part two:", part2())
