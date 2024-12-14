from collections import defaultdict

# filename = "sample.txt"
# height = 7
# width = 11

filename = "input.txt"
height = 103
width = 101

grid = []
part1_result = defaultdict(int)
part2_result = set()

with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        if line:
            parts = line.split()
            p = tuple(map(int, parts[0][2:].split(',')))
            v = tuple(map(int, parts[1][2:].split(',')))
            grid.append([p, v])
# print(grid)
rows, cols = len(grid), len(grid[0])
# print(rows, cols)


def move_robots(start_point, speed, times):
    x, y = start_point
    vx, vy = speed
    nx = x + vx * times
    ny = y + vy * times
    if ny < 0 or ny > height - 1:
        ny = ny % height
    if nx < 0 or nx > width - 1:
        nx = nx % width
    part1_result[(nx, ny)] += 1
    if (nx, ny) not in part2_result:
        part2_result.add((nx, ny))


def part1():
    for item in grid:
        start_point, speed = item
        move_robots(start_point, speed, 100)
    left_top_corner = 0
    left_down_corner = 0
    right_top_corner = 0
    right_down_corner = 0
    # print(width // 2, height // 2)
    # print(part1_result)
    for key, value in part1_result.items():
        x, y = key
        if x < width // 2 and y < height // 2:
            left_top_corner += value
        elif x < width // 2 and y > height // 2:
            left_down_corner += value
        elif x > width // 2 and y < height // 2:
            right_top_corner += value
        elif x > width // 2 and y > height // 2:
            right_down_corner += value
    # print(left_top_corner, left_down_corner, right_top_corner, right_down_corner)
    total = left_top_corner * left_down_corner * right_top_corner * right_down_corner
    return total


def check_christmas():
    total_check_nodes = 0
    for x, y in part2_result:
        total_check_nodes += (((x - 1, y) in part2_result) + ((x + 1, y) in part2_result) +
                              ((x, y - 1) in part2_result) + ((x, y + 1) in part2_result))
    return total_check_nodes


def part2():
    part2_times = 0
    part2_result_max = set()
    part2_check_nodes = 0
    for i in range(10000):  # 10000 is a magic number, it's a guess number
        # print(i)
        for item in grid:
            start_point, speed = item
            move_robots(start_point, speed, i)
        if part2_check_nodes < check_christmas():
            part2_check_nodes = check_christmas()
            part2_times = i
            part2_result_max = part2_result.copy()
        part2_result.clear()
    result_graph = []
    for y in range(height):
        for x in range(width):
            if (x, y) in part2_result_max:
                result_graph.append('#')
            else:
                result_graph.append(' ')
        result_graph.append('\n')
    print("".join(result_graph))
    return part2_times


print("Part one:", part1())
print("Part two:", part2())
