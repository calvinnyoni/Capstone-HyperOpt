import argparse

def main():
    """
    Function to create argparse object to get CLI arguments and invoke relevant functions based on these
    :return: none
    """
    pass

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as ex:
        print(ex)
        exit(1)

    exit(0)
