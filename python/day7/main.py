import re
from itertools import product
filename = "input.txt"
# filename = "sample.txt"
data = []
valid_data = []

with open(filename) as file:
    for line in file:
        numbers = list(map(int, re.findall(r"\d+", line.strip())))
        data.append(numbers)
print(data)


def check_valid(line_data, flag="part1"):
    target = line_data[0]
    check_combinations(line_data[1:], target)


def check_combinations(line_data, target, flag="part1"):
    # print(line_data)
    if flag == "part2":
        operators = list(product(['+', '*', '||'], repeat=len(line_data) - 1))
    else:
        operators = list(product(['+', '*'], repeat=len(line_data) - 1))
    comb_result = [0] * len(operators)
    for i in range(len(operators)):
        # print(operators[i])
        ops = operators[i]
        comb_result[i] = line_data[0]
        for j in range(len(ops)):
            # print(line_data[j], ops[j], line_data[j + 1])
            if ops[j] == '+':
                comb_result[i] += line_data[j + 1]
            elif ops[j] == '*':
                comb_result[i] *= line_data[j + 1]
            elif ops[j] == '||':
                comb_result[i] = int(str(comb_result[i]) + str(line_data[j + 1]))
        if comb_result[i] == target:
            valid_data.append(target)
            return
    # print(comb_result)


def part1():
    # check_valid(data[1])
    for line_data in data:
        check_valid(line_data)
    total = sum(valid_data)
    return total


def part2():
    for line_data in data:
        check_valid(line_data, "part2")
    total = sum(valid_data)
    return total


print("Part one:", part1())
print("Part two:", part2())
