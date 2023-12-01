import argparse

def get_args():
    """ Function : get_args
    parameters used in .add_argument
    1. metavar - Provide a hint to the user about the data type.
    - By default, all arguments are strings.

    2. type - The actual Python data type
    - (note the lack of quotes around str)

    3. help - A brief description of the parameter for the usage

    """

    parser = argparse.ArgumentParser(
    description='Example for Two positional arguments',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # Adding our first argument player name of type string
    parser.add_argument('player',
    metavar='player',
    type=str,
    help='Tennis Player')

    # Adding our second argument player titles of type integer/number.
    parser.add_argument('titles',
    metavar='titles',
    type=int,
    help='Tennis Player Grandslam Titles')

    return parser.parse_args()

# define main
def main(player, titles):
    print(f" *** The {player} had won {titles} grandslam titles.")

if __name__ == '__main__':
    args = get_args()
    main(args.player, args.titles)
