from time import perf_counter
start = perf_counter()

with open('input_day19.txt') as file:
    data = [line.strip().split(', ') for line in file.readlines()]

available_patterns = set(data[0])
requested_patterns = [line[0] for line in data[2:]]

biggest_available_pattern = max(len(item) for item in available_patterns)
smallest_available_pattern = min(len(item) for item in available_patterns)

solvable_dict = {}


def is_solvable(requested_pattern):
    if requested_pattern in solvable_dict.keys():
        ways_to_solve = solvable_dict[requested_pattern]

    elif len(requested_pattern) == 0:
        ways_to_solve =  1

    else:
        ways_to_solve = 0
        for size in range(smallest_available_pattern, min(len(requested_pattern), biggest_available_pattern) + 1):
            if requested_pattern[:size] in available_patterns:
                ways_to_solve += is_solvable(requested_pattern[size:])

        solvable_dict[requested_pattern] = ways_to_solve

    return ways_to_solve


print(sum((is_solvable(requested_pattern) > 0) for requested_pattern in requested_patterns))
print(sum(is_solvable(requested_pattern) for requested_pattern in requested_patterns))
print(perf_counter() - start)
