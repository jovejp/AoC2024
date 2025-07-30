import heapq

filename = "input.txt"
# filename = "sample.txt"
with open(filename) as file:
    lines = file.readlines()

tuples_list = [tuple(map(int, line.strip().split(','))) for line in lines]

# print(tuples_list)

# rows, cols = 7, 7
# ex, ey = 6, 6
# run_time = 12

rows, cols = 71, 71
ex, ey = 70, 70
run_time = 1024
grid = [["." for _ in range(cols)] for _ in range(rows)]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def print_g(graph):
    for row in graph:
        # print(row)
        print("".join(row))


visited = {}


def dijkstra():
    start_node = (0, 0)
    visited[start_node] = 0
    pq = []
    heapq.heappush(pq, (0, start_node))
    while pq:
        cost, (x, y) = heapq.heappop(pq)

        if visited.get((x, y), float("inf")) < cost:
            continue

        for i in range(4):
            dx, dy = directions[i]
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != "#":
                new_cost = cost + 1
                if new_cost < visited.get((nx, ny), float("inf")):
                    visited[(nx, ny)] = new_cost
                    heapq.heappush(pq, (new_cost, (nx, ny)))


def part1():
    # print_g(grid)
    index = 0
    while index < run_time:
        y, x = tuples_list[index]
        # print("x, y:", y, x)
        grid[x][y] = "#"
        index += 1
    # print("index:", index, tuples_list[index])
    # print_g(grid)
    dijkstra()
    # print("visited:", visited)
    return visited[(ex, ey)]


def part2():
    # print("part2")
    # print(visited)
    # print_g(grid)
    index = run_time
    while index < len(tuples_list):
        y, x = tuples_list[index]
        # print("x, y:", y, x)
        grid[x][y] = "#"
        index += 1
        if (x, y) in visited:
            if ((y - 1 < 0 or grid[x][y - 1] == "#") and (y + 1 >= cols or grid[x][y + 1] == "#")
                    or (x - 1 < 0 or grid[x - 1][y] == "#") and (x + 1 >= rows or grid[x + 1][y] == "#")):
                # print("seems find x, y:", x, y)
                visited.clear()
                dijkstra()
                if (ex, ey) not in visited:
                    return y, x
                # print("visited:", visited)


print("Part one:", part1())
print("Part two:", part2())
