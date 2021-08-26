import argparse

def main():
    """
    Function to create argparse object to get CLI arguments and invoke relevant functions based on these
    :return: none
    """
    pass

#CarlSAT Output Parser
def parseCost(text):
    textList = text.split("\n")

    stringList = textList[-2].split()

    time = float(stringList[-2])

    stringList = textList[-3].split()

    score = float(stringList[-1])

    return score + time

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as ex:
        print(ex)
        exit(1)

    exit(0)
