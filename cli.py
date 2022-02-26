from argparse import ArgumentParser

SOLVE_COMMAND = "solve"
SEARCH_COMMAND = "search"


def create_main_parser():
    parser = ArgumentParser()

    sub_parser = parser.add_subparsers(dest="cmd")

    run = sub_parser.add_parser(SOLVE_COMMAND, help="solve an instance of the sgp")
    search = sub_parser.add_parser(SEARCH_COMMAND, help="search for the optimized w value and write results to a file")

    create_run_parser(run)
    create_search_parser(search)

    return parser


def create_run_parser(parser):
    parser.add_argument('-g', "--group", dest='group', type=int, required=True, help="Pass the number of group as a parameter")
    parser.add_argument('-s', "--size", dest='group_size', type=int, required=True, help="Pass the size of a group as a parameter")
    parser.add_argument('-w', "--week", dest='week', type=int, required=True, help="Pass the number of group as a parameter")

    parser.add_argument('-n','--name', dest='name', help="use a given model")

    return parser


def create_search_parser(parser):

    parser.add_argument('-g', "--group", dest='group', type=int, required=True, help="Pass the number of group as a parameter")
    parser.add_argument('-s', "--size", dest='group_size', type=int, required=True, help="Pass the size of a group as a parameter")

    parser.add_argument('-o', "--out", dest='file', type=str, required=True, help="Path to export the results")

    parser.add_argument('-n','--name', dest='name', help="use a given model")

    return parser