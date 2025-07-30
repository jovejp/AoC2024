from typing import List, Dict, Tuple, Set, Optional
import numpy as np
from itertools import permutations

filename = "input.txt"
# filename = "sample.txt"
with open(filename) as file:
    g = [line.strip() for line in file.readlines()]


# Positions on keypads using numpy arrays for vectors
POSITIONS = {
    '7': np.array([0, 0]),
    '8': np.array([0, 1]),
    '9': np.array([0, 2]),
    '4': np.array([1, 0]),
    '5': np.array([1, 1]),
    '6': np.array([1, 2]),
    '1': np.array([2, 0]),
    '2': np.array([2, 1]),
    '3': np.array([2, 2]),
    '0': np.array([3, 1]),
    'A': np.array([3, 2]),
    '^': np.array([0, 1]),
    'a': np.array([0, 2]),  # 'A' in directional keypad
    '<': np.array([1, 0]),
    'v': np.array([1, 1]),
    '>': np.array([1, 2])
}

# Movement vectors
DIRECTIONS = {
    '^': np.array([-1, 0]),
    'v': np.array([1, 0]),
    '<': np.array([0, -1]),
    '>': np.array([0, 1])
}


def sequence_to_moveset(start: np.ndarray, end: np.ndarray, avoid: np.ndarray = np.array([0, 0])) -> List[str]:
    delta = end - start
    moves = []

    # Get required moves in each direction
    dx = delta[0]
    dy = delta[1]
    if dx < 0:
        moves.extend(['^'] * abs(dx))
    else:
        moves.extend(['v'] * dx)
    if dy < 0:
        moves.extend(['<'] * abs(dy))
    else:
        moves.extend(['>'] * dy)

    # Try all permutations of moves
    valid_sequences = []
    for p in set(permutations(moves)):
        positions = [start]
        valid = True
        for move in p:
            next_pos = positions[-1] + DIRECTIONS[move]
            if np.array_equal(next_pos, avoid):
                valid = False
                break
            positions.append(next_pos)
        if valid:
            valid_sequences.append(''.join(p) + 'a')

    return valid_sequences if valid_sequences else ['a']


ml_memos = {}


def min_length(sequence: str, limit: int = 2, depth: int = 0) -> int:
    memo_key = (sequence, depth, limit)
    if memo_key in ml_memos:
        return ml_memos[memo_key]

    avoid = np.array([3, 0]) if depth == 0 else np.array([0, 0])
    current = POSITIONS['A'] if depth == 0 else POSITIONS['a']

    total_length = 0
    for char in sequence:
        next_pos = POSITIONS[char]
        movesets = sequence_to_moveset(current, next_pos, avoid)

        if depth >= limit:
            total_length += len(min(movesets, key=len))
        else:
            min_moves = float('inf')
            for moveset in movesets:
                try:
                    length = min_length(moveset, limit, depth + 1)
                    min_moves = min(min_moves, length)
                except RecursionError:
                    continue
            if min_moves == float('inf'):
                # If no valid sequences found, use shortest direct path
                total_length += len(min(movesets, key=len))
            else:
                total_length += min_moves

        current = next_pos

    ml_memos[memo_key] = total_length
    return total_length


def calculate_complexity(code: str, sequence_length: int) -> int:
    numeric_part = int(''.join(c for c in code if c.isdigit()))
    return sequence_length * numeric_part


def part1():
    total_complexity = 0
    for code in g:
        length = min_length(code, limit=2)  # Default depth limit
        complexity = calculate_complexity(code, length)
        total_complexity += complexity
    return total_complexity


def part2():
    total_complexity = 0
    for code in g:
        length = min_length(code, limit=25)  # Higher depth limit
        complexity = calculate_complexity(code, length)
        total_complexity += complexity
    return total_complexity


print("Part one:", part1())
print("Part two:", part2())
