from collections import defaultdict

filename = "input.txt"
# filename = "sample.txt"
init_data = defaultdict(int)
with open(filename) as file:
    first_line = file.readline().strip()
    line_data = list(map(int, first_line.split()))


for data in line_data:
    init_data[data] += 1

rows = len(init_data)
print(init_data)


def convert(item):
    rep_data = []
    item_str = str(item)
    if item == 0:
        rep_data.append(1)
    elif len(item_str) % 2 == 0:
        half = len(item_str) // 2
        rep_data.append(int(item_str[:half]))
        rep_data.append(int(item_str[half:]))
    else:
        rep_data.append(2024 * item)
    return rep_data


# not perfect but works
# better to use an async function to all items in the dict
# and then sum the results
def run(curr_data_dict):
    rep_list = defaultdict(int)
    for item in curr_data_dict:
        item_value = curr_data_dict[item]
        for rep_item in convert(item):
            rep_list[rep_item] += item_value
    return rep_list


def part1():
    part1_data = init_data.copy()
    for i in range(25):
        part1_data = run(part1_data)
    print(sum(part1_data.values()))
    return sum(part1_data.values())


def part2():
    part2_data = init_data.copy()
    for i in range(75):
        part2_data = run(part2_data)
    return sum(part2_data.values())


print("Part one:", part1())
print("Part two:", part2())


