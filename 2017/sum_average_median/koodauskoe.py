"""Program that calculates as well as make comparisons of sum, average and median of numbers in input file"""
import sys

def exception_handler(exception_type, exception, traceback):
    """Remove traceback from exceptions for better UX"""
    print("%s: %s" % (exception_type.__name__, exception))

def get_args():
    """Get and verify command line arguments. Returns [filename, sum|avg|median, gt|lt|eq|None, number|None]"""
    # verify that there are enough arguments
    if (len(sys.argv) < 3):
        raise IndexError('Missing command line arguments! Correct usage: koodauskoe.py <tiedoston nimi> <sum|avg|median> [<gt|lt|eq> <n>]')

    # optional arguments used
    if (len(sys.argv) >= 4):          
        # verify 2nd optional argument
        try:
            optnum = int(sys.argv[4])            
        except ValueError:
            try:
                optnum = float(sys.argv[4])

            except ValueError:
                raise ValueError('Invalid optional argument! Fourth argument needs to be an integer or float, instead received "' + sys.argv[4] + ', which is ' + str(type(sys.argv[4])) + '".\n Correct usage: koodauskoe.py <tiedoston nimi> <sum|avg|median> [<gt|lt|eq> <n>]')
        except IndexError:
            raise IndexError('Missing 2nd optional argument! Correct usage: koodauskoe.py <tiedoston nimi> <sum|avg|median> [<gt|lt|eq> <n>]')

        args = [sys.argv[1], sys.argv[2], sys.argv[3], optnum]
        # verify 1st optional argument
        if (args[2] != 'gt' and args[2] != 'lt' and args[2] != 'eq'):
            raise ValueError('Invalid optional argument! Third argument needs to be either "gt", "lt" or "eq", instead received "' + str(args[2]) + '".\n Correct usage: koodauskoe.py <tiedoston nimi> <sum|avg|median> [<gt|lt|eq> <n>]')
        
    # no optional arguments
    else:
        args = [sys.argv[1], sys.argv[2], None, None]

    # verify 2nd argument
    if (args[1] != 'sum' and args[1] != 'avg' and args[1] != 'median'):
        raise ValueError('Invalid 2nd argument! Correct usage: koodauskoe.py <tiedoston nimi> <sum|avg|median> [<gt|lt|eq> <n>]')

    return args

def get_lines_from_file(filename):
    """Returns list of lines from file"""
    if (type(filename) != str):
        raise TypeError('get_lines_from_file expects string as input! Instead received ' + str(type(filename)) + '.')

    try:
        with open(filename, 'r') as infile:
            lines = map(lambda line: line.strip(), infile.read().strip().splitlines())
            return list(filter(lambda line: line != '', lines))

    except FileNotFoundError:
        raise FileNotFoundError('No file "' + filename + '" found. Please check that path and filename is correct.')

def avg(nums):
    """returns float average of list of numbers"""
    if (type(nums) != list):
        raise TypeError('"avg" expects list of ints as input! Instead received ' + str(type(nums)) + '.')

    return sum(nums)/len(nums)

def median(nums):
    """returns integer or tuple of 2 ints as median of list of numbers"""
    if (type(nums) != list):
        raise TypeError('"median" expects list of ints as input! Instead received ' + str(type(nums)) + '.')

    nums = sorted(nums)
    length = len(nums)
    if (length % 2 == 0):
        return (nums[int(length / 2) - 1], nums[int(length / 2)])
    else:
        return nums[int(length / 2)]

def get_comparison_result_finnish(operand, num1, num2):
    """return result of comparison of two numbers as string in finnish"""
    if (operand == 'gt'):
        if (num1 > num2):
            return str(num1) + ' on suurempi kuin ' + str(num2)

        else:
            return str(num1) + ' ei ole suurempi kuin ' + str(num2)

    elif (operand == 'lt'):
        if (num1 < num2):
            return str(num1) + ' on pienempi kuin ' + str(num2)

        else:
            return str(num1) + ' ei ole pienempi kuin ' + str(num2)

    elif (operand == 'eq'):
        if (num1 == num2):
            return str(num1) + ' on yhtä suuri kuin ' + str(num2)

        else:
            return str(num1) + ' ei ole yhtä suuri kuin ' + str(num2)

    else:
        raise ValueError('"get_comparison_result_finnish" accepts only "gt", "lt" or "eq" as operands. Instead received ' + str(operand) + 'of type ' + str(type(operand)) + '.')


def main():
    """Main Function"""
    # remove traceback for more user friendly exception messages
    sys.excepthook = exception_handler

    # get command line arguments
    filename, operation, comparison, optnum = get_args()

    # get lines from file
    try:
        nums = list(map(lambda line: int(line), get_lines_from_file(filename)))

    except (TypeError, ValueError):
        lines = get_lines_from_file(filename)
        for line in lines:
            if (not line.isdigit()):
                raise ValueError('Input file must be populated with lines of integers to work! Instead found ' + line + '.')

        raise

    if (operation == 'sum'):
        result = sum(nums)
        print('Summa on: ' + str(result))
        if (comparison != None):
            print(get_comparison_result_finnish(comparison, result, optnum))

    elif (operation == 'avg'):
        result = avg(nums)
        print('Keskiarvo on: ' + str(result))
        if (comparison != None):
            print(get_comparison_result_finnish(comparison, result, optnum))

    else:
        result = median(nums)
        if (type(result) == tuple):
            print('Mediaani on: ' + str(result[0]) + ' ja ' + str(result[1]))

        else:
            print('Mediaani on: ' + str(result))

        if (comparison != None):
            print(get_comparison_result_finnish(comparison, result[0], optnum))
            print(get_comparison_result_finnish(comparison, result[1], optnum))

if __name__ == "__main__":
    main()