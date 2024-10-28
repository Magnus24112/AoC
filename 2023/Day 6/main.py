with open('input.txt') as file:
    data = file.readlines()

data = [line.split()[1:] for line in data]
data = [(int(data[0][i]), int(data[1][i])) for i in range(len(data[0]))]

def n_ways_to_beat_record(time, record_distance) -> int:
    winning_holddowntimes = 0
    for holddowntime in range(1, time):
        distance = holddowntime * (time - holddowntime)
        if distance > record_distance:
            winning_holddowntimes += 1
    return winning_holddowntimes

def main():
    output = 1
    for time, record_distance in data:
        output *= n_ways_to_beat_record(time, record_distance)
    print(output)

if __name__ == '__main__':
    main()