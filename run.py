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
    name = args.name

    return Model(formula, group, group_size, week, name)


def run(model):

    with Lingeling(bootstrap_with=model.formula.clauses, with_proof=True) as solver:
        is_sat = solver.solve()
        print(is_sat)
        
        if not is_sat:
            print("UNSAT")
        else:
            result = model.decode_results(solver.get_model())
            solution = model.get_solution(result)
            instance = model.display(solution)

            # print(instance)

if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    model = create_model(args)


    model.generate_formula()
    print(len(model.formula.clauses))
    print(model.formula.nv)

    run(model)