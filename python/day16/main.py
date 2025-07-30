import heapq
from collections import deque

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

rows, cols = len(g), len(g[0])
# 0 1 2 3
# left,right, down, up
# N,E,S,W（北、东、南、西）
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

visited = {}
shortest_path = set()


def print_g(graph):
    for row in graph:
        # print(row)
        print("".join(row))


# print_g(g)


def dijkstra():
    start_node = (sx, sy, 1)
    visited[start_node] = 0
    pq = []
    heapq.heappush(pq, (0, start_node))
    while pq:
        cost, (x, y, direction) = heapq.heappop(pq)

        if visited.get((x, y, direction), float("inf")) < cost:
            continue

        # 直行
        dx, dy = directions[direction]
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and g[nx][ny] != "#":
            new_cost = cost + 1
            if new_cost < visited.get((nx, ny, direction), float("inf")):
                visited[(nx, ny, direction)] = new_cost
                heapq.heappush(pq, (new_cost, (nx, ny, direction)))

        # 左转 or 右转
        for nd in [(direction - 1) % 4, (direction + 1) % 4]:
            new_cost = cost + 1000
            if new_cost < visited.get((x, y, nd), float("inf")):
                visited[(x, y, nd)] = new_cost
                heapq.heappush(pq, (new_cost, (x, y, nd)))


def part1():
    dijkstra()
    return min(visited[(ex, ey, direction)] for direction in range(4) if (ex, ey, direction) in visited)


def find_shortest_path():
    min_cost = min(visited[(ex, ey, direction)] for direction in range(4) if (ex, ey, direction) in visited)
    q = deque()
    for d in range(4):
        if (ex, ey, d) in visited and visited[(ex, ey, d)] == min_cost:
            shortest_path.add((ex, ey, d))
            q.append((ex, ey, d))
    while q:
        x, y, d = q.popleft()
        curr_cost = visited[(x, y, d)]

        # 直行
        dx, dy = directions[d]
        nx, ny = x - dx, y - dy
        if 0 <= nx < rows and 0 <= ny < cols and g[nx][ny] != "#":
            prev_cost = curr_cost - 1
            if prev_cost >= 0:
                if (nx, ny, d) in visited and visited[(nx, ny, d)] == prev_cost:
                    shortest_path.add((nx, ny, d))
                    q.append((nx, ny, d))

        # 左转 or 右转
        curr_change_cost = curr_cost - 1000
        if curr_change_cost >= 0:
            for nd in [(d - 1) % 4, (d + 1) % 4]:
                if (x, y, nd) in visited and visited[(x, y, nd)] == curr_change_cost:
                    shortest_path.add((x, y, nd))
                    q.append((x, y, nd))


def part2():
    find_shortest_path()
    return len({(x, y) for x, y, _ in shortest_path})


print("Part one:", part1())
print("Part two:", part2())
