from collections import defaultdict, deque
import heapq

filename = "input.txt"
# filename = "sample.txt"
with open(filename) as file:
    g = [list(line.strip()) for line in file.readlines()]

sx, sy = next(
    ((row_index, col_index) for row_index, row in enumerate(g) for col_index, cell in enumerate(row) if cell == "S"),
    None)
print("start point:", sx, sy)

ex, ey = next(((row_index, col_index) for row_index, row in enumerate(g) for col_index, cell in enumerate(row) if
               cell == "E"), None)
print("end point:", ex, ey)

base_cost = []

rows, cols = len(g), len(g[0])
# 0 1 2 3
# left,right, down, up
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

WALLS = set()

for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        if g[i][j] == '#':
            WALLS.add((i, j))


def cached_dijkstra(node):
    pq = []
    heapq.heappush(pq, (0, node))
    cached_dict = defaultdict(int)
    cached_dict[node] = 0
    while pq:
        cost, (x, y) = heapq.heappop(pq)
        if cached_dict.get((x, y), float("inf")) < cost:
            continue
        for i in range(4):
            dx, dy = directions[i]
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and g[nx][ny] != "#":
                new_cost = cost + 1
                if new_cost < cached_dict.get((nx, ny), float("inf")):
                    cached_dict[(nx, ny)] = new_cost
                    heapq.heappush(pq, (new_cost, (nx, ny)))
    return cached_dict


cached_from_start = cached_dijkstra((sx, sy))
cached_from_end = cached_dijkstra((ex, ey))


def dijkstra(start_node, end_node):
    pq = []
    heapq.heappush(pq, (0, start_node))
    visited_nodes = defaultdict(int)
    visited_nodes[start_node] = 0

    while pq:
        cost, (x, y) = heapq.heappop(pq)
        if (x, y) == end_node:
            return cost
        if visited_nodes.get((x, y), float("inf")) < cost:
            continue
        if base_cost and cost > base_cost[0] - save_time:
            continue
        for i in range(4):
            dx, dy = directions[i]
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and g[nx][ny] != "#":
                new_cost = cost + 1
                if new_cost < visited_nodes.get((nx, ny), float("inf")):
                    visited_nodes[(nx, ny)] = new_cost
                    heapq.heappush(pq, (new_cost, (nx, ny)))
    return -1


saving_patterns = defaultdict(int)
saving_nodes = defaultdict(int)


def cheat_simc(limited_steps=2):
    for sr in range(rows):
        for sc in range(cols):
            if (sr, sc) in WALLS or (sr, sc) not in cached_from_start:
                continue
            # find end node
            queue = deque()
            queue.append((0, (sr, sc)))
            visited = set()
            while queue:
                cost, current_node = queue.popleft()
                if cost > limited_steps:
                    continue
                x, y = current_node
                if (x, y) not in WALLS and (x, y) in cached_from_end:
                    total_cost = cached_from_start[(sr, sc)] + cached_from_end[(x, y)] + cost
                    if total_cost < base_cost[0]:
                        gap_time = base_cost[0] - total_cost
                        saving_nodes[((sr, sc), (x, y))] = gap_time
                        saving_patterns[gap_time] += 1

                if cost < limited_steps:
                    for idx in range(4):
                        dx, dy = directions[idx]
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                            visited.add((nx, ny))
                            queue.append((cost + 1, (nx, ny)))


# save_time = 0
save_time = 100


def part1():
    cost = dijkstra((sx, sy), (ex, ey))
    if cost != -1:
        base_cost.append(cost)
    else:
        print("Error!!!, No path found")
        return 0
    cheat_simc()
    # print(saving_patterns)
    return sum(value for key, value in saving_patterns.items() if key >= save_time)


def part2():
    saving_nodes.clear()
    saving_patterns.clear()
    cheat_simc(20)
    # print(saving_patterns)
    return sum(value for key, value in saving_patterns.items() if key >= save_time)


print("Part one:", part1())
print("Part two:", part2())
