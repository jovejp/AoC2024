import re
# filename = "input.txt"
filename = "sample.txt"
with open(filename) as file:
    grid = [list(line.strip()) for line in file.readlines()]


rows, cols = len(grid), len(grid[0])


def part1():
    return 0


def part2():
    return 0


print("Part one:", part1())
print("Part two:", part2())
