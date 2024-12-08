filename = "input.txt"
# filename = "sample.txt"
with open(filename) as file:
    grid = [list(line.strip()) for line in file.readlines()]

rows, cols = len(grid), len(grid[0])
print(rows, cols)

filled_cells = set()
chars_cells = {}
sharp_cells = set()
sharp_cells_2 = set()

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == ".":
            continue
        else:
            filled_cells.add((i, j))
            if grid[i][j] in chars_cells:
                chars_cells[grid[i][j]].append((i, j))
            else:
                chars_cells[grid[i][j]] = [(i, j)]


def get_sharp_cells(chars_list):
    for i in range(len(chars_list)):
        for j in range(i + 1, len(chars_list)):
            x1, y1 = chars_list[i]
            x2, y2 = chars_list[j]
            dx, dy = x2 - x1, y2 - y1

            s = 0
            # loop down
            while True:
                x, y = x2 + dx * s, y2 + dy * s
                if 0 <= x < rows and 0 <= y < cols:
                    if s == 1:
                        sharp_cells.add((x, y))
                    sharp_cells_2.add((x, y))
                    s = s + 1
                else:
                    break

            s = 0
            # loop up
            while True:
                x, y = x1 - dx * s, y1 - dy * s
                if 0 <= x < rows and 0 <= y < cols:
                    if s == 1:
                        sharp_cells.add((x, y))
                    sharp_cells_2.add((x, y))
                    s = s + 1
                else:
                    break


def part1():
    for item_list in chars_cells.values():
        get_sharp_cells(item_list)
    return len(sharp_cells)


def part2():
    return len(sharp_cells_2)


print("Part one:", part1())
print("Part two:", part2())
