from time import perf_counter
start = perf_counter()

with open('input_day23.txt') as file:
    data = tuple(set(line.strip().split('-')) for line in file.readlines())


groups = set()
for i, connection in enumerate(data):
    for connection2 in data[i + 1:]:
        shared_element = connection & connection2
        if (shared_element and
            any(name[0] == 't' for name in connection.union(connection2)) and
            connection.union(connection2) - shared_element in data):
                groups.add(frozenset(connection.union(connection2)))


print(len(groups))
print(perf_counter() - start)