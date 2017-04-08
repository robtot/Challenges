"""Calculate Hypotenuse Exercise Solution"""
# plays sober (read: flawless!) Martti Suosalo game with the given number of
# players and turns.Takes number of players as first command line parameter
# and number of turns as second command line parameter

import sys

# check that command line arguments have been defined
if (len(sys.argv) < 3):
    print('Command line variables not defined. Program requires number of\n' +
    'players as first command line variable and number of turns as second\n' +
    'command line variable to function.')
    exit()

# class for iterating through players and defining direction
class PlayerCycleIterator:
    def __init__(self, numplayers):
        self.max = numplayers
        self.player = numplayers
        self.forwardDirection = True

    def changeDirection(self):
        self.forwardDirection = False

    def next(self):
        if (self.forwardDirection == True):
            if (self.player == self.max):
                self.player = 1
                return self.player
            else:
                self.player += 1
                return self.player
        else:
            if (self.player == 1):
                self.player = self.max
                return self.player
            else:
                self.player -= 1
                return self.player

# method for checking if "Martti Suosalo" should be printed
def isMarttiSuosalo(x):
    # check if number is divisible by 7
    if (x % 7 == 0):
        return True

    # check if contains '7' in digits
    xdigits = list(str(x))
    if '7' in xdigits:
        return True

    # check if digits sum is 7
    xdigits = list(map(int, xdigits))
    if sum(xdigits) == 7:
        return True

    # else return false
    return False

# check if all digits are the same
def allDigitsSame(x):
    if x < 10:
        return False

    xdigits = list(str(x))
    if (all(xdigits[0] == digit for digit in xdigits)):
        return True
    else:
        return False


# print header
print('nPlayers: ' + sys.argv[1] + '    nRounds: ' + sys.argv[2])

# initialize player iterator with number of players from command line argument
playerIterator = PlayerCycleIterator(int(sys.argv[1]))

# get number of turns from command line argument
turns = int(sys.argv[2])

# iterate through all turns
for i in range(1, turns + 1):
    # get next player turn
    player = playerIterator.next()

    # change direction if all digits are same
    if allDigitsSame(i):
        playerIterator.changeDirection()

    # output result
    if isMarttiSuosalo(i):
        print('P : ' + str(player) + '  "Martti Suosalo"')
    else:
        print('P : ' + str(player) + '  "' + str(i) + '"')
