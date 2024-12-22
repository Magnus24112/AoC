from time import perf_counter
import numpy as np

with open('input_day22.txt') as file:
    data = tuple(int(line) for line in file.readlines())


def evolve_secret_numbers(numbers):
    for _ in range(2000):
        numbers = numbers ^ (numbers << 6) & 16777215 # multiply by 64
        numbers = numbers ^ (numbers >> 5) & 16777215 # divide by 32
        numbers = numbers ^ (numbers << 11) & 16777215 # multiply by 20248
    return numbers


# part 1
start = perf_counter()
print(sum(evolve_secret_numbers(np.array(data))))
print(perf_counter() - start)
