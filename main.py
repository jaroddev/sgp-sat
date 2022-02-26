from cli import create_main_parser, SOLVE_COMMAND, SEARCH_COMMAND
from run import run
from search import search


if __name__ == "__main__":
    parser = create_main_parser()
    args = parser.parse_args()

    if args.cmd == SOLVE_COMMAND:
        run(args)
    elif args.cmd == SEARCH_COMMAND:
        search(args)
    else:
        parser.print_help()