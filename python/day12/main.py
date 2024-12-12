from collections import defaultdict
from collections import deque

filename = "input.txt"
# filename = "sample.txt"
with open(filename) as file:
    grid = [list(line.strip()) for line in file.readlines()]

rows, cols = len(grid), len(grid[0])

sub_areas = defaultdict(list)
sub_area_s = defaultdict(int)
sub_area_c = defaultdict(int)
sub_area_c2 = defaultdict(int)
visited_nodes = set()

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up


def bfs(x, y):
    start_value = grid[x][y]
    queue = deque([(x, y)])
    connected_nodes = []

    while queue:
        cx, cy = queue.popleft()
        if (cx, cy) in visited_nodes:
            continue
        visited_nodes.add((cx, cy))
        connected_nodes.append((cx, cy))
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited_nodes:
                if grid[nx][ny] == start_value:
                    queue.append((nx, ny))
    return connected_nodes


def get_last_key_with_char(char):
    for item_key in reversed(list(sub_areas.keys())):
        if item_key:
            if char in item_key:
                return item_key
        else:
            return None
    return None


def get_c(sub_area):
    total_c = 0
    for node in sub_area:
        x, y = node
        tmp_c = 4
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) in sub_area:
                tmp_c -= 1
        total_c += tmp_c
    return total_c


def get_c2(sub_area):
    total_c = 0
    for node in sub_area:
        x, y = node
        tmp_c = 4
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) in sub_area:
                tmp_c -= 1
            else:
                if dx == 0:
                    if (x+1, y) in sub_area and (x+1, ny) not in sub_area:
                        tmp_c -= 1
                elif dy == 0:
                    if (x, y+1) in sub_area and (nx, y+1) not in sub_area:
                        tmp_c -= 1
                else:
                    print("Error!!!", x, y, dx, dy)
        total_c += tmp_c
    return total_c


for i in range(rows):
    for j in range(cols):
        if (i, j) not in visited_nodes:
            item_value = grid[i][j]
            last_key = get_last_key_with_char(item_value)
            if last_key is None:
                new_key = item_value + str(1)
            else:
                new_key = item_value + str(int(last_key[1:]) + 1)
            sub_areas[new_key] = bfs(i, j)
            sub_area_s[new_key] = len(sub_areas[new_key])
            sub_area_c[new_key] = get_c(sub_areas[new_key])
            sub_area_c2[new_key] = get_c2(sub_areas[new_key])


def part1():
    total_sum = 0
    for key_s in sub_area_s:
        if key_s in sub_area_c:
            total_sum += sub_area_s[key_s] * sub_area_c[key_s]
            # print(key_s, sub_area_s[key_s], sub_area_c[key_s], sub_area_s[key_s] * sub_area_c[key_s])
    return total_sum


def part2():
    total_sum = 0
    for key_s in sub_area_s:
        if key_s in sub_area_c2:
            total_sum += sub_area_s[key_s] * sub_area_c2[key_s]
            # print(key_s, sub_area_s[key_s], sub_area_c2[key_s], sub_area_s[key_s] * sub_area_c2[key_s])
    return total_sum


print("Part one:", part1())
print("Part two:", part2())
