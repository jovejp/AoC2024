from collections import deque

filename = "input.txt"
# filename = "sample.txt"
with open(filename) as file:
    grid = [list(line.strip()) for line in file.readlines()]

empty_line_index = grid.index([])
g = grid[:empty_line_index]
d = grid[empty_line_index + 1:]
rows, cols = len(g), len(g[0])
g2 = []
g3 = []
for i in range(rows):
    temp_row = []
    temp_str = ""
    for item in g[i]:
        if item == "@":
            temp_str += "@."
            temp_row.append("@")
            temp_row.append(".")
        elif item == "#":
            temp_str += "##"
            temp_row.append("#")
            temp_row.append("#")
        elif item == ".":
            temp_str += ".."
            temp_row.append(".")
            temp_row.append(".")
        elif item == "O":
            temp_str += "[]"
            temp_row.append("[")
            temp_row.append("]")
    g2.append(temp_row)
    g3.append(temp_str)
rows_2, cols_2 = len(g2), len(g2[0])

sx, sy = next(
    ((row_index, col_index) for row_index, row in enumerate(g) for col_index, cell in enumerate(row) if cell == "@"),
    None)
print("start point for part1:", sx, sy)

sx2, sy2 = next(((row_index, col_index) for row_index, row in enumerate(g2) for col_index, cell in enumerate(row) if
                 cell == "@"), None)
print("start point for part2:", sx2, sy2)


move_dict = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}


def find_swap_point(x, y, dx, dy):
    bx, by = x - dx, y - dy
    while True:
        x += dx
        y += dy
        if x < 1 or x >= rows - 1 or y < 1 or y >= cols - 1:
            return bx, by
        elif g[x][y] == ".":
            return x, y
        elif g[x][y] == "#":
            return bx, by
        elif g[x][y] == "O":
            continue


def simc_move(x, y, direction):
    dx, dy = move_dict[direction]
    nx, ny = x + dx, y + dy
    if nx < 1 or nx >= rows - 1 or ny < 1 or ny >= cols - 1:
        return x, y
    else:
        if g[nx][ny] == ".":
            return nx, ny
        elif g[nx][ny] == "#":
            return x, y
        elif g[nx][ny] == "O":
            nnx, nny = find_swap_point(nx, ny, dx, dy)
            if nnx == x and nny == y:
                return x, y
            elif nnx != nx or nny != ny:
                grid[nx][ny], grid[nnx][nny] = ".", "O"
                return nx, ny
            else:
                print("Error!!!", x, y, dx, dy, nx, ny, nnx, nny)


def print_g(graph):
    for row in graph:
        # print(row)
        print("".join(row))


def sum_gps():
    total = 0
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if g[i][j] == "O":
                total += 100 * i + j
    return total


def part1():
    x, y = sx, sy
    for i in range(len(d)):
        for nd in d[i]:
            nx, ny = simc_move(x, y, nd)
            if (nx, ny) != (x, y):
                g[x][y], g[nx][ny] = ".", "@"
                x, y = nx, ny
    # print_g(g)
    return sum_gps()


def check_move_in_h(x, y, dy):
    bx, by = x, y - dy
    while True:
        y += dy
        if y < 2 or y >= cols_2 - 2:
            return bx, by
        elif g2[x][y] == ".":
            return x, y
        elif g2[x][y] == "#":
            return bx, by
        elif g2[x][y] == "]" or g2[x][y] == "[":
            continue


def check_move_in_v(x, y, dx):
    nnx = x
    queue = deque([(x, y)])
    check_v = True
    move_nodes = []
    while queue and check_v:
        nx, ny = queue.popleft()
        move_nodes.append((nx, ny))
        nx += dx
        if dx == -1:
            nnx = min(nnx, nx)
        elif dx == 1:
            nnx = max(nnx, nx)
        else:
            print("nnx Error!!!")
        # print("move_in_v", x, y, dx, nx, ny, g2[nx][ny])
        if nx < 1 or nx >= rows_2 - 1:
            check_v = False
        elif g2[nx][ny] == "#":
            check_v = False
        elif g2[nx][ny] == "]":
            queue.append((nx, ny))
            queue.append((nx, ny - 1))
        elif g2[nx][ny] == "[":
            queue.append((nx, ny))
            queue.append((nx, ny + 1))
        # else:
        #     print("valid .", g2[nx][ny])
    if check_v:
        # print("check_move_in_v", x, y, ly, my, nnx, move_nodes)
        return nnx, move_nodes
    else:
        return x, move_nodes


def simc_move_2(x, y, direction):
    dx, dy = move_dict[direction]
    nx, ny = x + dx, y + dy
    # print("simc_move_2", x, y, dx, dy, nx, ny, g2[nx][ny])
    if nx < 1 or nx >= rows_2 - 1 or ny < 2 or ny >= cols_2 - 2:
        return x, y
    else:
        if g2[nx][ny] == ".":
            g2[x][y], g2[nx][ny] = ".", "@"
            return nx, ny
        elif g2[nx][ny] == "#":
            return x, y
        elif g2[nx][ny] == "[" or g2[nx][ny] == "]":
            if dx == 0:
                # move in horizontal
                nnx, nny = check_move_in_h(nx, ny, dy)
                # print("----- move in horizontal-----", x, y, dx, dy, nx, ny, nnx, nny)
                if nny == y:
                    return x, y
                elif nny != ny:
                    # move in row
                    if dy == -1:  # move left
                        g2[nx][nny: y] = g2[nx][nny + 1:y + 1]
                    elif dy == 1: # move right
                        g2[nx][ny:nny + 1] = g2[nx][y:nny]
                    else:
                        print("Error!!!", x, y, dx, dy, nx, ny, nnx, nny)
                    g2[x][y] = "."  # clear the current position
                    return nx, ny
                else:
                    print("Error!!!", x, y, dx, dy, nx, ny, nx, nny)
            elif dy == 0:
                nnx, move_nodes = check_move_in_v(x, y, dx)
                move_nodes = list(set(move_nodes))
                # print("----- move in vertical-----", x, y, dx, dy, nnx, move_nodes)
                if nnx == x:
                    # no move in vertical
                    return x, y
                elif nnx != x:
                    # print("nnx", nnx, "x", x, "dx", dx)
                    while nnx != x:
                        nnx -= dx
                        subset = [node for node in move_nodes if node[0] == nnx]
                        for tx, ty in subset:
                            g2[tx+dx][ty], g2[tx][ty] = g2[tx][ty], "."
                    return nx, ny


def sum_gps_2():
    total = 0
    for i in range(1, rows_2 - 1):
        for j in range(1, cols_2 - 1):
            if g2[i][j] == "[":
                total += 100 * i + j
    return total


def part2():
    # print_g(g2)
    x, y = sx2, sy2
    for i in range(len(d)):
        for j, nd in enumerate(d[i]):
            # print(j, x, y, nd, move_dict[nd])
            nx, ny = simc_move_2(x, y, nd)
            x, y = nx, ny
    # print_g(g2)
    return sum_gps_2()


print("Part one:", part1())
print("Part two:", part2())
