import time
start = time.perf_counter()

with open('input.txt') as file:
    data = file.readlines()

readings = [[[int(item) for item in line.split()]] for line in data]


def getnextdifferences(currentdifferences: list) -> list:
    nextdifferences = []
    for number0, number1 in zip(currentdifferences, currentdifferences[1:]):
        nextdifferences.append((number1 - number0))
    return nextdifferences

for i, reading in enumerate(readings):
    while not all(difference == 0 for difference in readings[i][0]):
        #print(readings[i][-1])
        readings[i].insert(0, getnextdifferences(readings[i][0]))


for i, valuelist in enumerate(readings):
    for j, differencelists in enumerate(valuelist):
        #'''
        if j == 0:
            readings[i][j].append(0)
        else:
            readings[i][j].append(readings[i][j][-1] + readings[i][j - 1][-1])
        #differencelist[i].append()
        '''
        print(i, j, differencelists)
        #'''

output = 0
for lst in readings:
    output += lst[-1][-1]
print(output)

end = time.perf_counter()
print(end - start)

'''
def main():
    


if __name__ == '__main__':
    main()
'''