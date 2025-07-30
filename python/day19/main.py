from collections import defaultdict
import heapq

filename = "input.txt"
# filename = "sample.txt"
with open(filename) as file:
    content = file.read()

part1, part2 = content.split('\n\n', 1)

towel_pattern = sorted([element.strip() for element in part1.split(',')], key=len, reverse=True)
design_inputs = part2.strip().split('\n')
max_pattern_length = max(len(element) for element in towel_pattern)

# print(towel_pattern)
# print(design_inputs)

available_patterns = defaultdict(list)


def find_patterns(index, element):
    pq = []
    heapq.heappush(pq, (index, element, []))
    remain_element_list = [element]
    while pq:
        index, element, tmp_solution = heapq.heappop(pq)
        i = 1
        while i <= max_pattern_length and i <= len(element):
            next_tmp_solution = tmp_solution.copy()
            # print("element[:i]", i, element[:i])
            if element[:i] in towel_pattern:
                next_tmp_solution.append(element[:i])
                remain_element = element[i:]
                if i < len(element):
                    if remain_element not in remain_element_list:
                        # print(index, remain_element, next_tmp_solution)
                        remain_element_list.append(remain_element)
                        heapq.heappush(pq, (index, remain_element, next_tmp_solution))
                else:
                    # print("find the solutions====", index, next_tmp_solution)
                    if next_tmp_solution not in available_patterns[index]:
                        available_patterns[index].append(next_tmp_solution)
                        return
                    else:
                        print("error!!!, already in the available_patterns", index, next_tmp_solution)
            i += 1


def part1():
    for index, element in enumerate(design_inputs):
        # print(index, element)
        find_patterns(index, element)
    return len(available_patterns)


def find_pattern_nums(element, visited):
    # print("element", element, visited.keys(), visited.values())
    total = 0
    i = 1
    while i <= max_pattern_length and i <= len(element):
        if element[:i] in towel_pattern:
            remain_element = element[i:]
            if i < len(element):
                if remain_element in visited:
                    # print("find remain_element items====", remain_element, visited[remain_element])
                    total += 1 * visited[remain_element]
                    visited[element] += total
                else:
                    remain_element_solutions = find_pattern_nums(remain_element, visited)
                    visited[remain_element] = remain_element_solutions
                    # print("visited remain_element items====", remain_element, visited[remain_element])
                    total += 1 * remain_element_solutions
                    visited[element] += total
                    # print("visited element items====", element, visited[element])
            else:
                visited[element] += 1
                total += 1
                # print("find the solutions====", element, visited.keys())
        i += 1
    return total


def part2():
    total_solutions = 0
    visited = defaultdict(int)
    for index, element in enumerate(design_inputs):
        visited.clear()
        solutions = find_pattern_nums(element, visited)
        # print(index, "element", element, "solutions", solutions)
        total_solutions += solutions
    return total_solutions


print("Part one:", part1())
print("Part two:", part2())
