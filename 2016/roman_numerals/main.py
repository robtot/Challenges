"""CodeEval Roman Numerals Challenge Solution"""
# this solution works only for numbers in the range 1-3999
import sys

# read input argument file
with open(sys.argv[1], 'r') as infile:
    LINES = infile.read().strip().splitlines()

# iterate through each line in file
for line in LINES:
    #initialize solution variable
    roman = ""

    # convert line to integer
    i = int(line)

    # Make Mi equal to number of 1000ths i is composed of (M in roman numbers)
    # and convert i to remainder of dividing i with 1000. In addition, convert
    # Mi to roman numeral and add it to solution.
    Mi = int(i / 1000)
    i = i % 1000
    roman += "M" * Mi

    # Get 100ths
    Ci = int(i / 100)
    i = i % 100

    # format 100ths into roman numerals
    if (Ci == 9):
        roman += "CM"
    elif (Ci == 4):
        roman += "CD"
    elif (Ci >= 5):
        roman += "D"
        Ci -= 5
        roman += "C" * Ci
    else:
        roman += "C" * Ci

    # get 10ths
    Xi = int(i / 10)
    i = i % 10

    # format 10ths into roman numerals
    if (Xi == 9):
        roman += "XC"
    elif (Xi == 4):
        roman += "XL"
    elif (Xi >= 5):
        roman += "L"
        Xi -= 5
        roman += "X" * Xi
    else:
        roman += "X" * Xi

    # get 1ths
    Ii = i

    # format 1ths into roman numerals
    if (Ii == 9):
        roman += "IX"
    elif (Ii == 4):
        roman += "IV"
    elif (Ii >= 5):
        roman += "V"
        Ii -= 5
        roman += "I" * Ii
    else:
        roman += "I" * Ii

    print(roman)
