from argparse import ArgumentParser


def create_parser():
    parser = ArgumentParser()

    parser.add_argument('-g', "--group", dest='group', type=int, required=True, help="Pass the number of group as a parameter")
    parser.add_argument('-s', "--size", dest='group_size', type=int, required=True, help="Pass the size of a group as a parameter")
    parser.add_argument('-w', "--week", dest='week', type=int, required=True, help="Pass the number of group as a parameter")

    # no real implementation for now, only one parser used
    parser.add_argument('-n','--name', dest='name', help="use a given model")

    return parser