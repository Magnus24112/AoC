with open('input.txt') as file:
    data = [line.strip().split('|') for line in file.readlines()]

cards = [(set(line[0].split()[2:]), set(line[1].split())) for line in data]

def card_worth(winning_numbers: set, card: set) -> int:
    worth = len(winning_numbers & card)
    if worth <= 1:
        return worth
    else:
        return 2 ** (worth - 1)

def main():
    total_worth = 0
    for winning_numbers, card in cards:
        total_worth += card_worth(winning_numbers, card)
    print(total_worth)

if __name__ == '__main__':
    main()