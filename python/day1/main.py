import re

"""
    Not super proud of the part 2 solution due to the many nested for() loops.
"""

filename = "day1.txt"
input = []

with open(filename) as file:
    input = [line.strip() for line in file.readlines()]


def part1():
    total = 0
    first = []
    second = []
    for line in input:
        line =re.split(r'\s+', line)
        first.append(line[0])  # add first digit to list
        second.append(line[1])
    first.sort()
    second.sort()
    for i in range(len(first)):
        total = total + abs(int(first[i]) - int(second[i]))

    return total


def part2():
    total = 0
    first = []
    second = []
    for line in input:
        line = re.split(r'\s+', line)
        print(line[0], line[1])
        first.append(line[0])  # add first digit to list
        second.append(line[1])

    first.sort()
    second.sort()
    for i in range(len(first)):
        print(first[i], second.count(first[i]))
        total = total + int(first[i]) * second.count(first[i])
    return total


print("Part one:", part1())
print("Part two:", part2())