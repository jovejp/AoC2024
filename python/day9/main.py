filename = "input.txt"
# filename = "sample.txt"
with open(filename) as file:
    grid = [list(line.strip()) for line in file.readlines()]


rows = len(grid[0])
print(rows)
input_list = []
input_list_2 = []


def convert_file():
    for i, value in enumerate(grid[0]):
        if i % 2 == 0:
            B = str(i // 2)
        else:
            B = '.'
        input_list_2.append((B, int(value)))
        for _ in range(int(value)):
            input_list.append(B)


def swap_part1(cov_chars):
    str_len = len(cov_chars)
    i = str_len - 1
    j = 0
    while i > j:
        if cov_chars[i] != '.':
            while True and i > j:
                if cov_chars[j] == '.':
                    cov_chars[j] = cov_chars[i]
                    cov_chars[i] = '.'
                    i -= 1
                    break
                else:
                    j += 1
        else:
            i -= 1
    return cov_chars


def checksum(cov_chars):
    sub_total = 0
    for index, value in enumerate(cov_chars):
        if value == '.':
            break
        else:
            sub_total += index * int(value)
    return sub_total


def part1():
    convert_file()
    cov_chars = input_list.copy()
    swap_part1(cov_chars)
    # print(cov_chars)
    return checksum(cov_chars)


def swap_part2():
    input_list_3 = [item for item in input_list_2 if item[1] != 0]
    len_adjust = 0
    i = len(input_list_3) - 1
    while i >= 0:
        e_v0, e_v1 = input_list_3[i]
        # print(i, (e_v0, e_v1), input_list_3)
        if e_v0 != '.':
            for j, (f_v0, f_v1) in enumerate(input_list_3):
                if i < j:
                    break
                if f_v0 == '.' and f_v1 >= e_v1:
                    input_list_3.insert(i, (f_v0, e_v1))
                    input_list_3.pop(i+1)
                    input_list_3.insert(j, (e_v0, e_v1))
                    if f_v1 - e_v1 > 0:
                        input_list_3[j + 1] = (f_v0, f_v1 - e_v1)
                        len_adjust += 1
                        i += 1
                    else:
                        input_list_3.pop(j + 1)
                        len_adjust -= 1
                    break
        i -= 1
    return input_list_3


def checksum_2(cov_chars):
    sub_total = 0
    i = 0
    for v0, v1 in cov_chars:
        # print(v0, v1)
        if v0 == '.':
            i += v1
        else:
            for j in range(v1):
                sub_total += int(v0) * i
                i += 1
    return sub_total


def part2():
    # print(input_list)
    result_list = swap_part2()
    return checksum_2(result_list)


print("Part one:", part1())
print("Part two:", part2())
