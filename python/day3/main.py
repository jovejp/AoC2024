filename = "input.txt"
# filename = "sample.txt"

with open(filename) as file:
    grid = [line.strip() for line in file.readlines()]


def part1():
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    total = 0

    for line in grid:
        elements =re.findall(pattern, line)
        for element in elements:
            x, y = map(int, element)
            total = total + x * y
    return total


def part2():
    pattern = r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)'
    numPattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    total = 0
    skip = 0
    for line in grid:
        elements =re.findall(pattern, line)
        for element in elements:
            if element == "do()":
                skip = 0
            elif element == "don't()":
                skip = 1
            else:
                if skip == 0:
                    x, y = map(int, re.findall(numPattern, element)[0])
                    total = total + x * y
    return total


print("Part one:", part1())
print("Part two:", part2())
