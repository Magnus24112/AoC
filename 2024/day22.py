from time import perf_counter
import sys
sys.setrecursionlimit(10000)
start = perf_counter()

with open('input_day22.txt') as file:
    data = tuple(int(line) for line in file.readlines())

def base10_to_base2(num: int) -> tuple:
    output = []
    for i in range(23, -1, -1):
        if num >= 2**i:
            num -= 2**i
            output.append(True)
        else:
            output.append(False)
    return tuple(output)


def base2_to_base10(num: tuple) -> int:
    return sum(num[-i -1] * 2**i for i in range(24))


def evolve_secret_number(num: tuple, n_evolutions: int = 1) -> tuple:
    if n_evolutions == 0:
        return num

    evolved_num = mul2048(div32(mul64(num)))
    return evolve_secret_number(evolved_num, n_evolutions - 1)


def bitxor(num1: tuple, num2: tuple) -> tuple:
    return tuple(item1 != item2 for item1, item2 in zip(num1, num2))


def mul64(num: tuple) -> tuple:
    return bitxor(num, num[6:] + (False, ) * 6)


def mul2048(num: tuple) -> tuple:
    return bitxor(num, num[11:] + (False, ) * 11)


def div32(num: tuple) -> tuple:
    return bitxor(num, (False,) * 5 + num[:-5])


print(sum(base2_to_base10(evolve_secret_number(base10_to_base2(number), 2000)) for number in data))
print(perf_counter() - start)