with open('input_day1.txt') as data:
    locations = data.readlines()
locations = list(zip(*[[int(item) for item in line.split()] for line in locations]))


def quicksort(unsorted: list | tuple) -> list:
    if is_sorted(unsorted):
        return unsorted
    pivot = unsorted[-1]
    higher = []
    lower = []
    for item in unsorted[:-1]:
        if item > pivot:
            higher.append(item)
        else:
            lower.append(item)
    #print(f'Lower: {lower}, Pivot: {pivot}, Higher: {higher}')
    return quicksort(lower) + [pivot] + quicksort(higher)


def is_sorted(lst: list | tuple) -> bool:
    length = len(lst)
    if length <= 1:
        return True
    else:
        for i in range(length - 1):
            if not lst[i] < lst[i + 1]:
                return False
        return True


#part 1
locations = (quicksort(locations[0]), quicksort(locations[1]))
total_difference = sum(map(lambda a, b: abs(a - b), locations[0], locations[1]))

print(f'Total difference:  {total_difference}')


#part 2
similarity_score = sum(item * locations[1].count(item) for item in locations[0])

print(f'Similarity score: {similarity_score}')


#alternative (very slow) method for part 2
'''
largest_number = max(locations[0][-1], locations[1][-1])
location1_count = np.array([locations[0].count(i) for i in range(largest_number)])
location2_count = np.array([i * locations[1].count(i) for i in range(largest_number)])

print(np.dot(location1_count, location2_count))
'''
