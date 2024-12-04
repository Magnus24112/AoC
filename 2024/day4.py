import re

with open('input_day4.txt') as data:
    horizontal = [line.strip() for line in data.readlines()]


def diagonal_coordinates(line, index, n_columns, diagonal_1_direction = True):
    # converts diagonal coordinates into normal x, y coordinates
    x = min(line, n_columns - 1) - index
    y = index + max(line - n_columns + 1, 0) if diagonal_1_direction else n_columns - 1 - index - max(line - n_columns + 1, 0)
    return x, y


vertical = [''.join(row) for row in zip(*reversed(horizontal))]

n_rows = len(horizontal)
n_columns = len(horizontal[0])

coordinates = [(i, j) for i in range(n_rows) for j in range(n_columns)]

diagonal_1 = list((''.join(horizontal[row][column] for row, column in coordinates if row + column == i) for i in range(n_rows + n_columns - 1)))
diagonal_2 = list((''.join(vertical[row][column] for column, row in coordinates if row + column == i) for i in range(n_rows + n_columns - 1)))


# part 1
n_xmas = 0
pattern = r'(?=(XMAS|SAMX))'
for line in horizontal + vertical + diagonal_1 + diagonal_2:
    n_xmas += len(re.findall(pattern, line))


# part 2
mas_1_coordinates = set()
pattern = r'(?=(MAS|SAM))'
for i, line in enumerate(diagonal_1):
    indexes = re.finditer(pattern, line)
    for index in indexes:
        # + 1 because we want to know the coordinates of the A
        mas_1_coordinates.add(diagonal_coordinates(i, index.start() + 1, n_columns, True))


mas_2_coordinates = set()
for i, line in enumerate(diagonal_2):
    indexes = re.finditer(pattern, line)
    for index in indexes:
        mas_2_coordinates.add(diagonal_coordinates(i, index.start() + 1, n_columns, False))


n_cross_mas = len(mas_1_coordinates & mas_2_coordinates)
print(f'Number of \'xmas\'-es: {n_xmas}')
print(f'Number of \'cross-mas\'-es: {n_cross_mas}')