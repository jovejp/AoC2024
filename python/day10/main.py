filename = "input.txt"
# filename = "sample.txt"
start_poses = set()
grid = []
with open(filename) as file:
    for line in file:
        grid.append([int(char) for char in line.strip()])

rows, cols = len(grid), len(grid[0])

for x in range(rows):
    for y in range(cols):
        if grid[x][y] == 0:
            start_poses.add((x, y))


move_poses = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(check_pos, curr_value, visited_nodes, full_path_nodes):
    x, y = check_pos
    queue = set()
    for move_pos in move_poses:
        new_x, new_y = x + move_pos[0], y + move_pos[1]
        if (0 <= new_x < rows and 0 <= new_y < cols
                and grid[new_x][new_y] == curr_value):
            if curr_value == 9:
                full_path_nodes.add((new_x,new_y))
            else:
                queue.add((new_x, new_y))
    while queue:
        bfs(queue.pop(), curr_value+1, visited_nodes, full_path_nodes)


def part1():
    total = 0
    for start_pos in start_poses:
        visited_nodes = set()
        visited_nodes.add(start_pos)
        full_path_nodes = set()
        bfs(start_pos, 1, visited_nodes, full_path_nodes)
        total += len(full_path_nodes)
    return total


def bfs2(check_pos, curr_value, visited_nodes, full_path_nodes):
    x, y = check_pos
    queue = set()
    for move_pos in move_poses:
        new_x, new_y = x + move_pos[0], y + move_pos[1]

        if (0 <= new_x < rows and 0 <= new_y < cols
                and grid[new_x][new_y] == curr_value):
            if curr_value == 9:
                path_copy = visited_nodes.copy()
                path_copy.append(check_pos)
                path_copy.append((new_x,new_y))
                # print("+++++++++++", path_copy)
                full_path_nodes.append(path_copy)
            else:
                queue.add((new_x, new_y))
    if queue:
        visited_nodes.append(check_pos)
    while queue:
        bfs2(queue.pop(), curr_value+1, visited_nodes, full_path_nodes)


def part2():
    total = 0
    full_path_nodes = list([])
    for start_pos in start_poses:
        visited_nodes = []
        bfs2(start_pos, 1, visited_nodes, full_path_nodes)
    total = len(full_path_nodes)
    return total


print("Part one:", part1())
print("Part two:", part2())
