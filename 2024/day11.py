from time import perf_counter
from collections import defaultdict

with open('input_day11.txt') as file:
    start_stones = set(int(num) for num in file.readline().split())

stones = defaultdict(int)
for num in start_stones:
    stones[num] = 1


def update(stones: dict) -> dict:
    updated_stones = defaultdict(int)
    for num in stones:
        length = len(str(num))

        if num == 0:
            updated_stones[1] += stones[0]

        elif length % 2 == 0: # split int
            middle = 10 ** (length // 2)
            right = num % middle
            left = (num - right) // middle
            updated_stones[left] += stones[num]
            updated_stones[right] += stones[num]

        else:
            updated_stones[num * 2024] = stones[num]

    return updated_stones


def update_n_times(stones, iterations):
    for i in range(iterations):
        stones = update(stones)
    return sum(stones[num] for num in stones)


start = perf_counter()
print(update_n_times(stones, 25))
print(perf_counter() - start)

start = perf_counter()
print(update_n_times(stones, 75))
print(perf_counter() - start)