with open('test_input.txt') as file:
    data = file.readlines()

readings = [[int(item) for item in line.split()] for line in data]

def getnextdifferences(currentdifferences: list, done = False) -> (list, bool):
    print(currentdifferences)
    nextdifferences = []
    for number0, number1 in zip(currentdifferences, currentdifferences[1:]):
        nextdifferences.append((number1 - number0))
    if all(difference == 0 for difference in nextdifferences):
        done = True
    while not done:
        getnextdifferences(nextdifferences, False)
    return [currentdifferences + [currentdifferences[-1] + nextdifferences[-1]]], True

def main():
    global currentdifferences
    #currentdifferences = readings[0]
    print(getnextdifferences(readings[1]))
    #for currentdifferences in readings:
    #    print(getnextdifferences(currentdifferences))


if __name__ == '__main__':
    main()