from time import perf_counter

with open('input_day7.txt') as data:
    equations = tuple(tuple((int(item) for item in line.replace(':', '').strip().split())) for line in data.readlines())
equations = tuple((line[0], list(line[1:])) for line in equations)

start = perf_counter()


def is_solvable(goal: int, values: list, concatenation: bool = False) -> bool:

    if len(values) == 1:
        return goal == values[0]

    elif goal <= 0:
        return False

    if concatenation:
        str_goal = str(goal)
        str_last_value = str((values[-1]))

        if (str_goal.endswith(str_last_value) and str_goal != str_last_value and
                is_solvable(int(str_goal[:-len(str_last_value)]), values[:-1], concatenation)):
            return True

    if goal % values[-1] == 0 and is_solvable(int(goal // values[-1]), values[:-1], concatenation):
        return True

    return is_solvable(goal - values[-1], values[:-1], concatenation)


print(f'Total calibration result: {sum(goal * is_solvable(goal, values) for goal, values in equations)}')
print(f'Total calibration result with concatenation: {sum(goal * is_solvable(goal, values, True) for goal, values in equations)}')

end = perf_counter()
print(f'Time: {end - start}')