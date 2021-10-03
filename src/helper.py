from datetime import datetime


def open_file(filename):
    """
    Open the specified file and read in the raw data. Triggers exceptions: FileNotFound when the
    specified file is not found or a general exception when there was an error opening the file.
    :param filename: the name of the file as a string, including the file extension
    :return: an array of lines
    """
    if (filename[-5:].lower() != 'wcard') and (filename[-4:].lower() != 'wcnf'):
        raise_exception("Invalid file extension entered..")

    inform("Attempting to locate file '%s'" % filename)

    try:
        file = open(filename, 'r')
        inform("File located in current working directory")
        file.close()
    except FileNotFoundError:
        raise_exception("File not found...")
    except Exception:
        raise_exception("File could not be opened...")


def get_timeout_duration(test_size):
    durations = {
                    'test-30': 1,
                    'test-100': 2,
                    'test-500': 10
                }

    return durations[test_size.strip()]


'''
def extract_from_file(lines):
    """
    Extracts the required fields from the input file to parse to the CarlSAT
    :param lines:
    :return:
    """
    inform("Reading in data...")
    elements = []
    num_routes = 0
    num_clauses = 0
    hard_constraint = 1000.0

    for line in lines:
        line = (line.strip()).split(' ')

        # first line with 'p' flag and skip any line with 'c' flag
        if line[0] == 'p':
            num_routes = int(line[2])
            num_clauses = int(line[3])
            hard_constraint = float(line[4])
        elif line[0] != 'c':
            elements.append(line[::-2])

            # compare constraint (found at 0 index) to given hard constraint

    inform("Done...")
    return elements, num_routes, num_clauses, hard_constraint
'''


def now():
    """
    Get current datetime and format it to our desired format
    :return: returns formatted time output e.g. [2021-08-26] [17:33:12]
    """
    formatted_time = (datetime.now()).strftime("[%Y-%m-%d] [%H:%M:%S]")
    return str(formatted_time) + "\t"


def inform(message):
    """
    Inform user of current program execution stage so long as it is within normal operation
    :param message:
    :return:
    """
    log("\033[32m\033[1m%s\033[0m" % message)


def warn(message):
    """
    Print warning message to console on recoverable exceptions
    :param message:message to be printed out to console
    """
    log("\033[33m\033[1m[WARNING] %s\033[0m" % message)


def raise_exception(message):
    """
    Print error message to console on non-recoverable exceptions and exit message
    :param message: message to be printed out to console
    """
    log("\033[91m\033[1m[ERROR] %s\033[0m" % message)


def log(message):
    """
    Generic method used when printing to console
    :param message: message to be printed out to console
    """
    print("%s%s" % (now(), message))
