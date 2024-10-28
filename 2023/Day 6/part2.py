with open('input.txt') as file:
    data = file.readlines()

data = [line.split()[1:] for line in data]
time = int(''.join(data[0]))
distance = int(''.join(data[1]))

def n_ways_to_beat_record(time, record_distance) -> int:
    winning_holddowntimes = 0
    for holddowntime in range(1, time):
        distance = holddowntime * (time - holddowntime)
        if distance > record_distance:
            winning_holddowntimes += 1
    return winning_holddowntimes

def main():
    output = n_ways_to_beat_record(time, distance)
    print(output)

if __name__ == '__main__':
    main()