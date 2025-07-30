import re
# filename = "input.txt"
filename = "sample.txt"
with open(filename) as file:
    grid = [list(line.strip()) for line in file.readlines()]
rows, cols = len(grid), len(grid[0])

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visited_place = {}
visited_place_direction = {}
block_place = [0]
new_block = []
simced_block = []


def get_next_direction(i):
    return directions[(i + 1) % 4]


def simc_move(start_point, start_direction):
    sx, sy = start_point
    x, y = start_point
    m1, m2 = start_direction
    while True:
        curr_direction = directions.index((m1, m2))
        if (x, y, curr_direction) in visited_place_direction:
            print("loop loop loop loop", x, y)
            return
        else:
            visited_place_direction[(x, y, curr_direction)] = 1
        if (x, y) in visited_place:
            visited_place[(x, y)] += 1

        else:
            visited_place[(x, y)] = 1
        if x + m1 < 0 or x + m1 >= rows or y + m2 < 0 or y + m2 >= cols:
            return
        elif grid[x + m1][y + m2] == '#':
            m1, m2 = get_next_direction(curr_direction)
        else:
            x += m1
            y += m2


def find_start():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '^':
                return (i, j)


def part1():
    print(grid)
    start_point = find_start()
    print(start_point)
    start_direction = 0
    simc_move(start_point, directions[start_direction])
    return len(visited_place)


def simc_move_2(start_point, start_direction, block_point):
    x, y = start_point
    m1, m2 = start_direction
    bx, by = block_point
    visited_place_direction_2 = {}
    while True:
        curr_direction = directions.index((m1, m2))
        if (x, y, curr_direction) in visited_place_direction_2:
            return 1
        else:
            visited_place_direction_2[(x, y, curr_direction)] = 1
        if x + m1 < 0 or x + m1 >= rows or y + m2 < 0 or y + m2 >= cols:
            return 0
        elif grid[x + m1][y + m2] == '#' or (x + m1 == bx and y + m2 == by):
            m1, m2 = get_next_direction(curr_direction)
        else:
            x += m1
            y += m2


def part2():
    start_point = find_start()
    start_direction = 0
    return sum(simc_move_2(start_point, directions[start_direction], block)
               for block in visited_place if block != start_point)


print("Part one:", part1())
print("Part two:", part2())
