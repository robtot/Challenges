"""CodeEval Set Intersection Challenge Solution"""
import sys

class SwapError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class ParseError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

def get_argv_input_file_lines():
    """Returns list of string lines from argv[1] file"""
    try:
        with open(sys.argv[1], 'r') as infile:
            return infile.read().strip().splitlines()

    except IndexError:
        raise ValueError('No command line argument supplied! Program requires command line argument to input file to function.')

    except FileNotFoundError:
        raise FileNotFoundError('No file at "' + sys.argv[1] + '" found. Check that path is correct.')

def swap_elements(container, index1, index2):
    """Swaps elements (indexes as 2nd and 3rd arguments) in list of numbers (1st argument)"""
    try:
        if (index1 < 0 or index2 < 0):
            raise SwapError('Invalid swap attempt with negative numbers. Negative numbers are not allowed!')

        element1 = container[index1]
        container[index1] = container[index2]
        container[index2] = element1
    except IndexError:
        raise SwapError('Index out of bounds when performing swap of '+str(index1)+' and '+str(index2)+' on '+str(container))

    except TypeError:
        msg = 'Expecting swap indexes as integers and container as list!\n'
        if (type(index1) != int):
            msg += 'First index is of type '+str(type(index1))+'!\n'

        if (type(index2) != int):
            msg += 'Second index is of type '+str(type(index2))+'!\n'

        if (type(container) != list):
            msg += 'Container is of type '+str(type(container))+'!\n'

        raise TypeError(msg)

def parse_swap_elements(line):
    """Parses string line and swaps elements accroding to challenge specification and retunrs result as string"""
    if (type(line) is not str):
        raise TypeError('Expecting string argument. Instead received ' + type(line))

    try:
        numbers, swaps = line.split(':')
        numbers = numbers.strip().split(' ')
        swaps = swaps.strip().split(', ')
        for swap in swaps:
            swap1, swap2 = swap.split('-')
            swap_elements(numbers, int(swap1), int(swap2))

    except ValueError:
        raise ParseError('Invalid format for parse_swap_elements: "' + line + '"')
    
    return ' '.join(numbers)

def main():
    """Main Function"""
    lines = get_argv_input_file_lines()
    for line in lines:
        print(parse_swap_elements(line))

if __name__ == "__main__":
    main()