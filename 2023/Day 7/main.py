import time
import os
os.chdir("/Users/Magnus/Documents/Python/Prog 2.1/Advent of Code/Day 7/")
start = time.perf_counter()

with open('input.txt') as file:
    data = file.readlines()

data = [line.split() for line in data]
data = [(list(hand), int(bet)) for (hand, bet) in data]

def handstrength(hand: list) -> int:
    '''
    Output: 0-6 where
    6: five of a kind
    5: four of a kind
    4: full house
    3: three of a kind
    2: two pair
    1: one pair
    0: high card
    '''
    cardfrequency = []
    for card in hand:
        cardfrequency.append(hand.count(card))
    '''
    #alternate method:
    cardfrequency = [cardfrequency.count(frequency) for frequency in range(2, 6)]
    #[number of cards with frequency 2, number of cards with frequency 3, ..., 5]
    if cardfrequency[3] >= 1:
        return 6
    elif cardfrequency[2] >= 1:
        return 5
    elif cardfrequency[1] >= 1 and cardfrequency[0] >= 1:
        return 4
    elif cardfrequency[1] >= 1:
        return 3
    elif cardfrequency[0] >= 4:
        return 2
    elif cardfrequency[0] >= 1:
        return 1
    else:
        return 0
    '''
    if cardfrequency[0] == 5:
        return 6
    elif 4 in cardfrequency:
        return 5
    elif 3 in cardfrequency and 2 in cardfrequency:
        return 4
    elif 3 in cardfrequency:
        return 3
    elif cardfrequency.count(2) == 4:
        return 2
    elif 2 in cardfrequency:
        return 1
    else:
        return 0
    #'''

def cardtonumber(card: str) -> int:
    '''
    converts card into a number
    '4' -> 4
    'K' -> 13
    'A' -> 14
    '''
    if card in ['9', '8', '7', '6', '5', '4', '3', '2']:
        return int(card)
    elif card == 'T':
        return 10
    elif card == 'J':
        return 11
    elif card == 'Q':
        return 12
    elif card == 'K':
        return 13
    else:
        return 14


def comparehands(hand1: list, hand1strength: int, hand2: list, hand2strength: int) -> bool:
    '''
    True if hand1 is stronger than hand2
    False is hand2 is stronger than (or the same as) hand1
    '''
    if hand1strength != hand2strength:
        return hand1strength > hand2strength
    else:
        for i in range(5):
            if hand1[i] != hand2[i]:
                return cardtonumber(hand1[i]) > cardtonumber(hand2[i])
        return False


def quicksort(unsorted: list) -> list:
    '''
    unsorted[0] looks like: [[card1, card2, ..., card5], handstrength, bet]
    '''
    if is_sorted(unsorted):
        return unsorted
    pivot = [unsorted[-1]]
    higherthanpivot = []
    lowerthanpivot = []
    for hand, strength, bet in unsorted[:-1]:
        if comparehands(hand, strength, pivot[0][0], pivot[0][1]):
            higherthanpivot.append((hand, strength, bet))
        else:
            lowerthanpivot.append((hand, strength, bet)) 
    return quicksort(lowerthanpivot) + pivot + quicksort(higherthanpivot)

def is_sorted(inputlist: list) -> bool:
    '''
    inputlist[0] looks like: [[card1, card2, ..., card5], handstrength, bet]
    '''
    length = len(inputlist)
    if length <= 1:
        return True
    else:
        for i in range(length-1):
            if not comparehands(inputlist[i+1][0], inputlist[i+1][1], inputlist[i][0], inputlist[i][1]):
                return False
        return True
            

def main():
    #[strength0, strength1, ..., strength6]
    datawithstrength = [[], [], [], [], [], [], []]
    for hand, bet in data:
        strength = handstrength(hand)
        datawithstrength[strength].append((hand, strength, bet))
    sorteddata = []
    for strength in datawithstrength:
        sorteddata.extend(quicksort(strength))
    puzzleoutput = 0
    for multiplier, (hand, strength, bet) in enumerate(sorteddata, 1):
        puzzleoutput += multiplier * bet
    print(puzzleoutput)
            

if __name__ == '__main__':
    main()



end = time.perf_counter()
print(end - start)