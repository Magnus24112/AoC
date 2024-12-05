with open('input_day5.txt') as data:
    pages = data.readlines()

order_rules = set(tuple(tuple(line.strip().split('|')) for line in pages[:pages.index('\n')]))
pages = tuple(tuple(line.strip().split(',')) for line in pages[pages.index('\n') + 1:])


def ordering(left, right):
    return not (right, left) in order_rules


def quicksort(unsorted: list | tuple, ordering) -> list:
    if is_sorted(unsorted, ordering):
        return unsorted
    pivot = unsorted[-1]
    higher = []
    lower = []
    for item in unsorted[:-1]:
        if ordering(item, pivot):
            lower.append(item)
        else:
            higher.append(item)
    return quicksort(lower, ordering) + [pivot] + quicksort(higher, ordering)


def is_sorted(lst: list | tuple, ordering) -> bool:
    length = len(lst)
    if length <= 1:
        return True
    else:
        for i in range(length - 1):
            if not ordering(lst[i], lst[i + 1]):
                return False
        return True


middle_pages = []
middle_pages_2 = []
for line in pages:
    if is_sorted(line, ordering):
        middle = int(line[int(len(line) / 2)])
        middle_pages.append(middle)
    else:
        sorted_list = quicksort(line, ordering)
        middle = int(sorted_list[int(len(line) / 2)])
        middle_pages_2.append(middle)


print(f'Middle sum of correctly-ordered updates: {sum(middle_pages)}')
print(f'Middle sum of incorrectly-ordered updates: {sum(middle_pages_2)}')