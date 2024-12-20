from collections import defaultdict
import numpy as np
import sys
from time import perf_counter

np.set_printoptions(linewidth=10000)
sys.setrecursionlimit(10000)
start = perf_counter()

with open('input_day20.txt') as file:
    maze = np.array(tuple(tuple(line.strip()) for line in file.readlines()))

max_row = len(maze) - 1
max_column = len(maze[0]) - 1

start_position = np.where(maze == 'S')
start_position = start_position[0][0], start_position[1][0]

end_position = np.where(maze == 'E')
end_position = end_position[0][0], end_position[1][0]
maze[end_position] = '.'

costs = np.full_like(maze, 1_000_000, dtype=int)


def solve_maze(current_position: tuple, current_cost: int, previous_position: tuple = tuple()):
    row, column = current_position
    costs[current_position] = current_cost

    if current_position == end_position:
        return

    for next_position in {(row +1, column), (row -1, column), (row, column +1), (row, column -1)} - {previous_position}:
        if maze[next_position] == '.':
            solve_maze(next_position, current_cost + 1, current_position)
            return


def get_all_cheats(max_distance) -> dict:
    cheats = defaultdict(int)
    possible_end_positions = set((i, j)
                                 for i in range(-max_distance, max_distance + 1)
                                 for j in range(-max_distance, max_distance + 1)
                                 if abs(i) + abs(j) <= max_distance) - {(0, 0)}

    for row_i, row in tuple(enumerate(costs))[1:-1]:
        for column_i, item in tuple(enumerate(row))[1:-1]:
            if item != 1_000_000:
                for diff_row, diff_column in possible_end_positions:
                    if 0 <= row_i + diff_row <= max_row and 0 <= column_i + diff_column <= max_column:
                        position = row_i + diff_row, column_i + diff_column
                        if costs[position] != 1_000_000:
                            time_saved = costs[position] - (item + abs(diff_row) + abs(diff_column))
                            if time_saved > 0:
                                cheats[time_saved] += 1
    return cheats


solve_maze(start_position, 0)

# part 1
cheats = get_all_cheats(2)
print(sum(cheats[time_saved] for time_saved in cheats if time_saved >= 100))
print(perf_counter() - start)

# part 2
cheats = get_all_cheats(20)
print(sum(cheats[time_saved] for time_saved in cheats if time_saved >= 100))
print(perf_counter() - start)