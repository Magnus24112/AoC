with open('input.txt') as file:
    data = [line.strip().split('|') for line in file.readlines()]

cards = [(set(line[0].split()[2:]), set(line[1].split())) for line in data]

def main():
    n_cards = len(cards)
    cards_amount = [1] * len(cards)
    
    for i, (winning_numbers, card) in enumerate(cards):
        worth = len(winning_numbers & card)
        
        for j in range(1, worth + 1):
            if i + j < n_cards: #prevent index out of range
                cards_amount[i + j] += cards_amount[i]

    print(sum(cards_amount))

if __name__ == '__main__':
    main()