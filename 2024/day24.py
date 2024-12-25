from time import perf_counter
start = perf_counter()

with open('test_input_day24.txt') as file:
    data = [line.strip() for line in file.readlines()]


gates = {}
wires = {}
append_to_gates = False

for line in data:
    if len(line) == 0:
        append_to_gates = True
    elif append_to_gates:
        gate = line.split()
        gates[gate[-1]] = tuple(gate[:3])
    else:
        wire, value = line.split(': ')
        wires[wire] = bool(int(value))


def get_wire_value(wire: str):
    if wire in wires:
        return

    wire1, operator, wire2 = gates[wire]

    get_wire_value(wire1)
    get_wire_value(wire2)

    match operator:
        case 'OR':
            wires[wire] = wires[wire1] | wires[wire2]
        case 'AND':
            wires[wire] = wires[wire1] & wires[wire2]
        case 'XOR':
            wires[wire] = wires[wire1] ^ wires[wire2]


answer = 0
for gate in gates:
    if gate.startswith('z'):
        get_wire_value(gate)
        if wires[gate]:
            answer += 2 ** int(gate[1:])


print(answer)
print(perf_counter() - start)