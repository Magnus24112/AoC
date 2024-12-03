from turtledemo.forest import doit1

with open('input_day3.txt') as data:
    memory = [list(line.strip()) for line in data.readlines()]


def multiplier(memory, conditional_statements = False):
    mul = ['m', 'u', 'l', '(', 'int1', ',', 'int2', ')']
    do = ['d', 'o', '(', ')']
    dont = ['d', 'o', 'n', '\'', 't', '(', ')']
    enabled = True

    left_mul = []
    right_mul = []
    for row_index, row in enumerate(memory):
        int1 = []
        int2 = []
        mul_index = 0

        len_row = len(row)

        for pointer, item in enumerate(row):
            #print(f'Item: {item} Correct: {mul[mul_index]} (Int1, Int2): {int1, int2} Enabled: {enabled}')
            #print(f'left mul {left_mul} right mul {right_mul}')


            if mul[mul_index] == 'int1' or mul[mul_index] == 'int2':
                if item == ',' and mul[mul_index] == 'int1':
                    mul_index += 2
                    #print('test2')
                elif item == ')':
                    if enabled and int1 != [] and int2 != []:
                        left_mul.append(int(''.join(int1)))
                        right_mul.append(int(''.join(int2)))
                    #print('test')
                    int1 = []
                    int2 = []
                    mul_index = 0
                    #print(left_mul, right_mul)
                else:
                    try:
                        if mul[mul_index] == 'int1':
                            int1.append(str(int(item)))
                        else:
                            int2.append(str(int(item)))
                    except ValueError:
                        #print('ValueError')
                        int1 = []
                        int2 = []
                        mul_index = 0

            elif item == mul[mul_index]:
                mul_index += 1

            elif conditional_statements:

                if len_row - pointer >= 4:
                    if [row[pointer], row[pointer + 1], row[pointer + 2], row[pointer + 3]] == do:
                        #print('DO!')
                        enabled = True
                if len_row - pointer >= 7:
                    if [row[pointer], row[pointer + 1], row[pointer + 2], row[pointer + 3], row[pointer + 4], row[pointer + 5], row[pointer + 6]] == dont:
                        #print('DON\'T!')
                        enabled = False

                int1 = []
                int2 = []
                mul_index = 0

            else:
                int1 = []
                int2 = []
                mul_index = 0

    return zip(left_mul, right_mul)

total_uncorrupted = sum(a * b for a, b in multiplier(memory, False))
total_uncorrupted_conditional = sum(a * b for a, b in multiplier(memory, True))

print(f'Total uncorrupted: {total_uncorrupted}')
print(f'Total uncorrupted with conditional functions: {total_uncorrupted_conditional}')