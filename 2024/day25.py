from time import perf_counter
start = perf_counter()

with open('input_day25.txt') as file:
    data = tuple(line.strip() for line in file.readlines())

keys = set()
locks = set()

for i in range(0, len(data), 8):
    column_totals = tuple(sum(data[i + row][column] == '#' for row in range(1, 6)) for column in range(5))

    if data[i][0] == '#':
        locks.add(column_totals)
    else:
        keys.add(column_totals)


combinations = 0
for lock in locks:
    for key in keys:
        combinations += all(key[i] + lock[i] <= 5 for i in range(5))

print(combinations)
print(perf_counter() - start)