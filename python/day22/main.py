
import math
from collections import defaultdict, deque

filename = "input.txt"
# filename = "sample.txt"
with open(filename) as file:
    input_data = [int(line.strip()) for line in file.readlines()]

cache_next_value = defaultdict(int)


def next_value(s) -> int:
    s = ((s * 64) ^ s) % 16777216
    s = ((math.floor(s / 32)) ^ s) % 16777216
    s = (s * 2048 ^ s) % 16777216
    return s


def next_value_2000(s) -> (int, list[int], list[int]):
    i = 0
    c_n = []
    c_g = []
    while i < 2000:
        if s in cache_next_value:
            s = cache_next_value[s]
        else:
            t = s
            s = ((s * 64) ^ s) % 16777216
            s = ((math.floor(s / 32)) ^ s) % 16777216
            s = (s * 2048 ^ s) % 16777216
            cache_next_value[t] = s
        c_n.append(s % 10)
        if i > 1:
            c_g.append(c_n[i] - c_n[i - 1])
        i += 1
    return s, c_n, c_g


cached_numbers = []
cached_gaps = []


def part1():
    total = 0
    for line in input_data:
        result, c_n, c_g = next_value_2000(line)
        # print(line, ":", result)
        cached_numbers.append(c_n)
        cached_gaps.append(c_g)
        total += result
    return total


def part2():
    total_list = defaultdict(int)
    visited_patterns = defaultdict(int)
    for i in range(len(cached_numbers)):
        for j in range(len(cached_gaps[i])-3):
            search_pattern = tuple(cached_gaps[i][j:j+4])
            if visited_patterns[search_pattern] != i:
                visited_patterns[search_pattern] = i
                total_list[search_pattern] += cached_numbers[i][j+5]
    return max(total_list.values())


print("Part one:", part1())
print("Part two:", part2())
