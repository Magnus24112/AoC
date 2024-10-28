import time
from math import prod as product
start = time.perf_counter()

with open('input.txt') as file:
    data = file.readlines()

directions = list(data[0].strip())
nodes = data[2:]
nodes2 = []
[nodes2.extend(line) for line in nodes]
nodes3 = []
tmp = []
tmp2 = []
for item in nodes2:
    if item.isalpha() or item.isnumeric():
        tmp.append(item)
        if len(tmp) == 3:
            tmp = (tmp[0] + tmp[1] + tmp[2])
            tmp2.append(tmp)
            tmp = []
            if len(tmp2) == 3:
                nodes3.append((tmp2[0], tuple(tmp2[1:])))
                tmp2 = []
#nodes3 = set(nodes3)
node_dict = {position: (left, right) for position, (left, right) in nodes3}
start_node_dict = {position: position for position, (left, right) in nodes3 if position.endswith('A')}


def nextposition(position: str, decision: str) -> str:
    '''
    node looks like: (currentposition, (positionifleft, positionifright))
    for example: ('AAA', ('BBB', 'CCC'))
    '''
    #nextpos = node[1][0] if decision == 'L' else node[1][1]
    '''for i, node in enumerate(nodes3):
        if node[0] == nextpos:
            return nodes3[i]'''
    #return 'Error, node not found'
    return node_dict.get(position)[1 if decision == 'R' else 0]


def main():
    global n_steps
    global len_directions
    len_directions = len(directions)
    n_steps_list = []
    for startpos in start_node_dict.keys():
        currentposition = startpos
        n_steps = 0
        while not currentposition.endswith('Z'):
            #print(currentposition)
            start_node_dict[startpos] = nextposition(currentposition, directions[n_steps%len_directions])
            currentposition = start_node_dict[startpos]
            n_steps += 1
        n_steps_list.append(n_steps/len_directions)
        #print(int(n_steps))
        #print(start_node_dict)
    #print(n_steps_list)
    print(int(len_directions * product(n_steps_list)))


if __name__ == '__main__':
    main()

end = time.perf_counter()
print(end - start)