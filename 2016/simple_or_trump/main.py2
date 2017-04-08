"""CodeEval Simple or Trump Challenge Solution"""
import sys

with open(sys.argv[1], 'r') as infile:
    LINES = infile.read().strip().splitlines()

def to_rank(value):
    """convert character card rank to numerical value"""
    if type(value) is int and value > 1 and value < 11:
        return value
    elif value == 'A':
        return 14
    elif value == 'K':
        return 13
    elif value == 'Q':
        return 12
    elif value == 'J':
        return 11
    else:
        print "ERROR: Illegal card value" + value + "in input file!"
        sys.exit()

#loop through lines in input file
for line in LINES:
    #assign values from input file to variables
    cards, trump = line.split('|', 1)
    cards = cards.strip().split(' ')
    trump = trump.strip()
    value1 = cards[0][0:-1]
    suit1 = cards[0][-1]
    value2 = cards[1][0:-1]
    suit2 = cards[1][-1]

    #determine if cards are trump
    if trump == suit1:
        trump1 = True
    else:
        trump1 = False
    if trump == suit2:
        trump2 = True
    else:
        trump2 = False

    #determine the higher ranked card
    if trump1 == True and trump2 == False:
        print cards[0]
    elif trump1 == False and trump2 == True:
        print cards[1]
    elif trump1 == True and trump2 == True:
        if value1 > value2:
            print cards[0]
        elif value2 > value1:
            print cards[1]
        else:
            print cards[0] + ' ' + cards[1]
    else:
        if value1 > value2:
            print cards[0]
        elif value2 > value1:
            print cards[1]
        else:
            print cards[0] + ' ' + cards[1]
