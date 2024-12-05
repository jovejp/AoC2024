import re

"""
    Not super proud of the part 2 solution due to the many nested for() loops.
"""

filename = "input.txt"
input = []

with open(filename) as file:
    input = [line.strip() for line in file.readlines()]


def part1():
    safe = 0
    for line in input:
        elements =re.split(r'\s+', line)
        print(elements)
        flag = 0
        check = 1
        for i in range(len(elements) -1):
            current_element = int(elements[i])
            next_element = int(elements[i + 1])
            if current_element < next_element:
                if flag == 2:
                    check = 0
                    break
                flag = 1
            elif current_element > next_element:
                if flag == 1:
                    check = 0
                    break
                flag = 2
            else:
                check = 0
                break
            gap = abs(current_element - next_element)
            if gap < 1 or gap > 3:
                check = 0
                break
        safe += check
    return safe


def part2():
    safe = 0
    for line in input:
        elements =re.split(r'\s+', line)
        print(elements)
        check = 1
        diff = 0
        greater = 0
        lower = 0
        equal = 0
        for i in range(len(elements) -1):
            current_element = int(elements[i])
            next_element = int(elements[i + 1])
            if current_element < next_element:
                lower = lower + 1

            elif current_element > next_element:
                greater = greater + 1
            else:
                equal = equal + 1
            gap = abs(current_element - next_element)
            if gap < 1 or gap > 3:
                diff = diff + 1
            if greater > lower:
                if lower + diff + equal > 1:
                    check = 0
                    break
            elif lower > greater:
                if greater + diff + equal > 1:
                    check = 0
        safe += check
    return safe


print("Part one:", part1())
print("Part two:", part2())
