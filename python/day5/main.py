import re

"""
    Not super proud of the part 2 solution due to the many nested for() loops.
"""


filename = "input.txt"
# filename = "sample.txt"
rules = {}
wait_check = []
validated_list = []
invalid_list = []
is_wait_check = False
with open(filename) as file:
    for line in file.readlines():
        line = line.strip()
        if not line:
            is_wait_check = True
            continue
        if not is_wait_check:
            key, value = map(int, line.split('|'))
            if key in rules:
                rules[int(key)].append(int(value))
            else:
                rules[int(key)] = [int(value)]
        else:
            numbers = list(map(int, line.split(',')))
            wait_check.append(numbers)
    grid = [line.strip() for line in file.readlines()]

# print("Rules:", rules)
# print("Wait Check:", wait_check)


def part1():
    total = 0
    for items in wait_check:
        is_valid = True
        for i in range(len(items) - 1, 0, -1):
            current_number = items[i]
            previous_numbers = items[:i]
            if any(num in rules.get(current_number, []) for num in previous_numbers):
                is_valid = False
                break
        if is_valid:
            validated_list.append(items)
            total += items[len(items) // 2]
    # print("Validated List:", validated_list)
    return total


def rearrange_numbers(data_for_sort, sort_rules):
    i = len(data_for_sort) - 1
    while i > 0:
        current_number = data_for_sort[i]
        previous_numbers = data_for_sort[:i]
        moved = False
        for j in range(i - 1, -1, -1):
            if previous_numbers[j] in sort_rules.get(current_number, []):
                data_for_sort.insert(i, data_for_sort.pop(j))
                moved = True
                break
        if not moved:
            i -= 1
    return data_for_sort


validated_list = []
invalid_list = []
def part2():
    total = 0
    for items in wait_check:
        is_valid = True
        for i in range(len(items) - 1, 0, -1):
            current_number = items[i]
            previous_numbers = items[:i]
            if any(num in rules.get(current_number, []) for num in previous_numbers):
                is_valid = False
                invalid_list.append(items)
                break
        # if is_valid:
            # validated_list.append(items)
    # print("invalid_list:", invalid_list)
    for items in invalid_list:
        items = rearrange_numbers(items, rules)
        validated_list.append(items)
        total += items[len(items) // 2]
    # print("validated_list:", validated_list)
    return total


print("Part one:", part1())
print("Part two:", part2())
