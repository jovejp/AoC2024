grid = []
result = []
found_positions = []
found_positions_2 = []
directions = [
    (0, 1), (1, 0), (1, 1), (1, -1),  # right, down, down-right, down-left
    (0, -1), (-1, 0), (-1, -1), (-1, 1)  # left, up, up-left, up-right
]
word = "XMAS"
word_len = len(word)

filename = "input.txt"
# filename = "sample.txt"
with open(filename) as file:
    grid = [line.strip() for line in file.readlines()]

rows, cols = len(grid), len(grid[0])


def search_direction(x, y, dx, dy):
    for i in range(word_len):
        if not (0 <= x < rows and 0 <= y < cols) or grid[x][y] != word[i]:
            return False
        x += dx
        y += dy
    return True


def search_word():
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                positions = search_direction(x, y, dx, dy)
                if positions:
                    found_positions.append((x, y))
    return found_positions


def part1():
    positions = search_word()
    return len(positions)


def search_direction_2(x, y):
    if grid[x][y] == 'A':
        for i in [-1, 1]:
            if not (0 <= x + i < rows) or not (0 <= y + i < cols):
                return False
        if ((grid[x + 1][y + 1] == 'M' and grid[x - 1][y - 1] == 'S') or
                (grid[x + 1][y + 1] == 'S' and grid[x - 1][y - 1] == 'M')):
            if ((grid[x + 1][y - 1] == 'M' and grid[x - 1][y + 1] == 'S') or
                    (grid[x + 1][y - 1] == 'S' and grid[x - 1][y + 1] == 'M')):
                return True
    return False


def search_word_2():
    for x in range(rows):
        for y in range(cols):
            positions_2 = search_direction_2(x, y)
            if positions_2:
                found_positions_2.append((x, y))
    return found_positions_2


def part2():
    positions = search_word_2()
    print(found_positions_2)
    return len(positions)


print("Part one:", part1())
print("Part two:", part2())
