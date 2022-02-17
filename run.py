from pysat.formula import CNF
from pysat.solvers import Lingeling

from model import Model
from cli import create_parser

# g - p - w
def create_model(args):
    formula = CNF()

    group = args.group
    group_size = args.group_size
    week = args.week

    return Model(formula, group, group_size, week)


def run(model):

    with Lingeling(bootstrap_with=model.formula.clauses, with_proof=True) as solver:
        res = solver.solve()
        print(res)
        
        if not res:
            print(solver.get_proof())
            print("UNSAT")
            exit(1)
        else:
            pos = model.decode_results(solver.get_model())
            print(pos)


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    model = create_model(args)


    model.generate_formula()
    print(len(model.formula.clauses))

    run(model)