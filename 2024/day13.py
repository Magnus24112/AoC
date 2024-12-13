import re
from time import perf_counter
start = perf_counter()


with open('input_day13.txt') as file:
    data = [line.strip() for line in file.readlines()]

data2 = []
for i in range(0, len(data), 4):
    data2.append(' '.join(data[i:i+4]))


def calculate_intersection(a1, b1, c1, a2, b2, c2):
    if (a1*c2 - a2*c1) % (a1*b2 - a2*b1) != 0:
        return False

    B = (a1*c2 - a2*c1) // ( a1*b2 - a2*b1)

    if (c1 - b1*B) % a1 != 0:
        return False

    A = (c1 - b1*B) // a1

    return A, B


def calculate_total_price(part2 = False):
    total_cost = 0
    for line in data2:
        a1, a2, b1, b2 = re.findall('(?<=\\+)[0-9]+', line)
        c1, c2 = re.findall('(?<==)[0-9]+', line)
        a1, b1, c1, a2, b2, c2 = int(a1), int(b1), int(c1), int(a2), int(b2), int(c2)

        if part2:
            c1 += 10000000000000
            c2 += 10000000000000

        button_presses = calculate_intersection(a1, b1, c1, a2, b2, c2)

        if button_presses:
            A, B = button_presses
            total_cost += 3*A + B

    return total_cost


print('Time to initialize:', perf_counter() - start)

start = perf_counter()
print('Part 1:', calculate_total_price())
print('Part 1 time:', perf_counter() - start)

start = perf_counter()
print('Part 2:', calculate_total_price(True))
print('Part 2 time:', perf_counter() - start)