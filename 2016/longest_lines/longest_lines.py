"""Solution for Longest Lines Challenge on CodeEval"""
import sys

with open(sys.argv[1], 'r') as infile:
    LINES = infile.read().strip().splitlines()

output_lines = int(LINES.pop(0))

LINES = sorted(LINES, key=lambda x: len(x), reverse=True)

for line in LINES:
    if output_lines <= 0:
        break
    print line
    output_lines = output_lines - 1
