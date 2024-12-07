from time import perf_counter
import copy
#from matplotlib import pyplot as plt

with open('input_day6.txt') as data:
    original_guard_map = [list(line.strip()) for line in data.readlines()]

start = perf_counter()


def solve_guard_map(guard_map):
    directions = ('up', 'right', 'down', 'left')
    direction = directions[0]
    locations_visited = set()

    n_rows = len(guard_map)

    # guard position = (x, y)
    x = 0
    y = 0
    for i, row in enumerate(guard_map):
        if '^' in row:
            x = row.index('^')
            y = i
            guard_map[y][x] = 'X'
            break

    guard_vision = tuple()
    inside_bounds = True

    while inside_bounds:

        if direction == 'up':
            guard_vision = tuple(reversed([guard_map[row][x] for row in range(0, y)]))

        elif direction == 'right':
            guard_vision = tuple(guard_map[y][x+1:])

        elif direction == 'down':
            guard_vision = tuple(guard_map[row][x] for row in range(y+1, n_rows))

        elif direction == 'left':
            guard_vision = tuple(reversed(guard_map[y][:x]))


        if not '#' in guard_vision:
            obstacle_index = len(guard_vision)
            inside_bounds = False
        else:
            obstacle_index = guard_vision.index('#')


        if direction == 'up':
            for row in range(1, obstacle_index+1):
                guard_map[y - row][x] = 'X'
            y -= obstacle_index

        elif direction == 'right':
            for column in range(1, obstacle_index+1):
                guard_map[y][x + column] = 'X'
            x += obstacle_index

        elif direction == 'down':
            for row in range(1, obstacle_index+1):
                guard_map[y + row][x] = 'X'
            y += obstacle_index

        elif direction == 'left':
            for column in range(1, obstacle_index+1):
                guard_map[y][x - column] = 'X'
            x -= obstacle_index

        direction = directions[(directions.index(direction) + 1) % 4]
        current_location = ((x, y), direction)

        if current_location in locations_visited:
            return 0, True, guard_map

        else:
            locations_visited.add(current_location)

    x_count = sum(row.count('X') for row in guard_map)
    return x_count, False, guard_map


def deepcopy(input_map):
    return [copy.copy(row) for row in input_map]


x_count, _, original_guard_map_solved = solve_guard_map(copy.deepcopy(original_guard_map))


looping_maps_count = 0

for row in range(len(original_guard_map)):

    for column in range(len(original_guard_map[0])):

        if original_guard_map_solved[row][column] == 'X' and original_guard_map[row][column] == '.':

            augmented_guard_map = deepcopy(original_guard_map)
            augmented_guard_map[row][column] = '#'

            if solve_guard_map(augmented_guard_map)[1]:
                looping_maps_count += 1


print(f'Number of squares visited: {x_count}')
print(f'Number of possible obstruction locations: {looping_maps_count}')
end = perf_counter()
print('Time:', end - start)

# Plot
'''
for (x, y), direction in locations_visited[:-1]:
    match direction:
        case 'up':
            marker = '^'
        case 'right':
            marker = '>'
        case 'down':
            marker = 'v'
        case 'left':
            marker = '<'

    plt.scatter(x, -y, marker = marker, color = 'black')
plt.show()
'''