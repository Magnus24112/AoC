import numpy as np
from time import perf_counter
start = perf_counter()

with open('input_day10.txt') as data:
    trails = np.array([tuple(int(item) for item in line.strip()) for line in data.readlines()])

trails = np.pad(trails, 1, constant_values=-1)
trailheads = set((int(left), int(right)) for left, right in zip(*np.where(trails == 0))) # row, column


neighbours = []
for row_i, row in enumerate(trails[1:-1]):
    neighbour_row = []
    for column_i, column in enumerate(row[1:-1]):
        # shape: [up, down, left, right]
        neighbour_row.append([int(trails[row_i][column_i + 1]),
                              int(trails[row_i + 2][column_i + 1]),
                              int(row[column_i]),
                              int(row[column_i + 2])])
    neighbours.append(neighbour_row)

neighbours = np.array(neighbours)


def trail_count(current_positions: set, current_height: int) -> set:
    # returns positions of trail ends for 1 trailhead (no duplicates)
    if current_height == 9:
        return current_positions

    next_positions = set()

    for row, column in current_positions:
        for direction, neighbour in enumerate(neighbours[row - 1][column - 1]):
            if neighbour == current_height +1:
                if direction == 0:
                    next_positions.add((row -1, column))
                elif direction == 1:
                    next_positions.add((row +1, column))
                elif direction == 2:
                    next_positions.add((row, column -1))
                elif direction == 3:
                    next_positions.add((row, column + 1))

    if next_positions:
        return trail_count(next_positions, current_height +1)
    else:
        return set()


def trail_quality(current_positions: list, current_height: int) -> list:
    # returns positions of trail ends for 1 trailhead (with duplicates)
    if current_height == 9:
        return current_positions

    next_positions = []

    for row, column in current_positions:
        for direction, neighbour in enumerate(neighbours[row - 1][column - 1]):
            if neighbour == current_height +1:
                if direction == 0:
                    next_positions.append((row -1, column))
                elif direction == 1:
                    next_positions.append((row +1, column))
                elif direction == 2:
                    next_positions.append((row, column -1))
                elif direction == 3:
                    next_positions.append((row, column + 1))

    if next_positions:
        return trail_quality(next_positions, current_height +1)
    else:
        return []


end = perf_counter()
print('Time to initialize:', end-start)

start = perf_counter()
print('Part 1:', sum(len(trail_count({position}, 0)) for position in trailheads))
print('Part 1 time:', perf_counter() - start)

start = perf_counter()
print('Part 2:', sum(len(trail_quality([position], 0)) for position in trailheads))
print('Part 2 time:', perf_counter() - start)