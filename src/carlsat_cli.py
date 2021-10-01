import sys
import helper
from tuner import tune


def main(filename, test_out):
    """
    Function to create argparse object to get CLI arguments and invoke relevant functions based on these
    :return: none
    """
    helper.inform("Starting file import and preprocessing..")
    helper.open_file(filename)

    helper.inform("File preprocessing done...\nSettting timeout settings..")
    timeout = helper.get_timeout_duration(test_out)
    print()
    tune(filename, timeout)


if __name__ == '__main__':
    from pymoo.configuration import Configuration
    Configuration.show_compile_hint = False
    '''
    try:
        if len(sys.argv) < 2:
            helper.raise_exception("Invalid arguments entered. Please enter arguments <filename> <timeout>")

        if sys.argv[2].strip() not in ['test-30', 'test-100', 'test-500']:
            helper.raise_exception("Invalid timeout test size specified")

        main(sys.argv[1], sys.argv[2])
    except KeyboardInterrupt as ex:
        helper.raise_exception(ex)
    '''

    exit(0)
