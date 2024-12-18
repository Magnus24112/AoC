from collections import defaultdict
import numpy as np
from time import perf_counter
start = perf_counter()


with open('input_day18.txt') as file:
    data = [line.strip().split(',') for line in file.readlines()]
data = tuple(tuple((int(right), int(left))) for left, right in data)


def next_step(current_positions, current_distance, visited_positions):
    global distances

    visited_positions = visited_positions.union(current_positions)

    current_neighbours = set()
    for position in current_positions:
        distances[position] = current_distance
        current_neighbours = current_neighbours.union(neighbours[position]) - visited_positions

    if end_position in current_neighbours:
        return current_distance + 1

    elif current_neighbours == set():
        return 'No solution found'

    return next_step(current_neighbours, current_distance + 1, visited_positions)


size = 71
start_position = (0, 0)
end_position = (size - 1, size - 1)

default_neighbours = defaultdict(set)
for row in range(size):
    for column in range(size):
        for position in {(row -1, column), (row +1, column), (row, column -1), (row, column +1)}:
            if -1 not in set(position) and size not in set(position):
                default_neighbours[(row, column)].add(position)


# part 1

start = perf_counter()
blockages = set(data[:1024])

neighbours = defaultdict(set)
for position in default_neighbours:
    neighbours[position] = default_neighbours[position] - blockages

distances = np.zeros((size, size))

solution = next_step({start_position}, 0, set())
print('Part 1 solution:', solution)
print('Part 1 time:', round(perf_counter() - start, 3), '\n')


# part 2

start = perf_counter()

lower_bound = 0
upper_bound = len(data) - 1


while True:
    n_bytes = (upper_bound + lower_bound) // 2
    blockages = set(data[:n_bytes])

    neighbours = defaultdict(set)
    for position in default_neighbours:
        #print(position, neighbours[position])
        neighbours[position] = default_neighbours[position] - blockages

    distances = np.zeros((size, size))

    solution = next_step({start_position}, 0, set())
    if solution == 'No solution found':
        upper_bound = n_bytes
    else:
        lower_bound = n_bytes

    if lower_bound + 1 == upper_bound:
        solution = data[upper_bound - 1]
        solution = solution[1], solution[0]
        break


print('Part 2 solution:', solution)
print('Part 2 time:', round(perf_counter() - start, 3))