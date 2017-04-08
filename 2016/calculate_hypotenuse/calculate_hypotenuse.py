"""Calculate Hypotenuse Exercise Solution"""
# Make a program, which reads from an input file length of legs (A and B) of a
# right-angled triangle. Calculate length of the hypotenuse using Pythagoras
# law (hypotenuse2 = legA2 + LegB2). Name of the input and output file is given
# as command line arguments.

import sys
import math

# read first command line argument file
with open(sys.argv[1], 'r') as infile:
    LINES = infile.read().strip().splitlines()

# remove first line (table header)
LINES.pop(0)

# initialize dictionary for solution data (to iterate in order of hypotenuse)
outData = dict()

# iterate through tasks in input file and solve for hypotenuse
for line in LINES:
    legAstr, legBstr = line.split(' ', 1)

    # convert input file data from feet to meters
    legA = float(legAstr) * 0.3048
    legB = float(legBstr) * 0.3048

    # perform mathemathical calculation
    hypotenuse = math.sqrt(legA**2 + legB**2)

    # format task solution for output
    outData[hypotenuse] = "%.2f" % legA + ' ' + "%.2f" % legB + ' ' + "%.4f" % hypotenuse

# output solution to second command line argument file
with open(sys.argv[2], 'w') as outfile:
    # write header to output file
    outfile.write('legA legB hypotenuse' + '\n')
    # write rows in ascending order of hypotenuse
    for key in sorted(outData.iterkeys()):
        outfile.write(outData[key] + '\n')
