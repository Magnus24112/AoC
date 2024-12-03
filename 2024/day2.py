from time import perf_counter
start = perf_counter()

with open('input_day2.txt') as data:
    reports = data.readlines()
reports = tuple(tuple(int(item) for item in line.split()) for line in reports)
#reports = [[1, 2, 3, 10, 4]]

def is_ascending_descending(lst: list | tuple) -> bool:
    # true if input is entirely ascending or descending
    ascending = lst[0] < lst[1]
    for i in range(1, len(lst) - 1):
        if ascending != (lst[i] < lst[i+1]):
            return False
    return True


def is_safe(lst: list | tuple, dampened = False) -> bool:
    len_lst = len(lst)
    differences = tuple(lst[i+1] - lst[i] for i in range(len_lst - 1))

    if max(differences) <= 3 and all(difference > 0 for difference in differences):
        return True
    elif min(differences)  >= -3 and all(difference < 0 for difference in differences):
        return True
    elif not dampened:
        return False
    else:
        '''
        print(lst)
        print(differences)

        # assumes ascending order
        safe_list = tuple(0 < difference <= 3 for difference in differences)
        print(safe_list)
        if sum(safe_list) == len_lst - 2:
            unsafe_index = safe_list.index(False)
            #print('unsafe index', unsafe_index)
            for i in range(2):
                #can just check items left and right to index
                test_lst = tuple(lst[j] for j in range(len_lst) if i + j != unsafe_index)
                if is_safe(test_lst):
                    return True
        elif sum(safe_list) == len_lst - 3:
            unsafe_index = safe_list.index(False)
            print('unsafe index', unsafe_index)
            if not safe_list[unsafe_index + 1]:
                test_lst = tuple(lst[i] for i in range(len_lst) if i != unsafe_index + 1)
                print(test_lst)
                if is_safe(test_lst):
                    return True


        # assumes ascending order
        safe_list = tuple(-3 <= difference < 0 for difference in differences)
        #print(safe_list)
        if sum(safe_list) == len_lst - 2:
            unsafe_index = safe_list.index(False)
            #print(unsafe_index)
            for i in range(2):
                test_lst = tuple(lst[j] for j in range(len_lst) if i + j != unsafe_index)
                if is_safe(test_lst):
                    return True
            return False
        elif sum(safe_list) == len_lst - 3:
            unsafe_index = safe_list.index(False)
            if not safe_list[unsafe_index + 1]:
                test_lst = tuple(lst[i] for i in range(len_lst) if i != unsafe_index + 1)
                if is_safe(test_lst):
                    return True

        return False
        '''
        for i in range(len_lst):
            test_lst = tuple(lst[j] for j in range(len_lst) if j != i)
            if is_safe(test_lst):
                return True
        return False



#for report in reports:
    #print('Safe:', is_safe(report, True))

total_safe_reports = sum(is_safe(report, True) for report in reports)
print(total_safe_reports)

end = perf_counter()
print(f'Time: {round(end - start, 5)}s')