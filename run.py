from time import time

from pysat.formula import CNF
from pysat.solvers import Lingeling

from model import Model


def run(args):
    model = create_model(args)
    start = time()
    model.generate_formula()
    solve(model)
    end = time()
    print("time: ", end - start)

# g - p - w
def create_model(args):
    formula = CNF()

    group = args.group
    group_size = args.group_size
    week = args.week
    name = args.name

    return Model(formula, group, group_size, week, name)


def solve(model):

    with Lingeling(bootstrap_with=model.formula.clauses, with_proof=True) as solver:
        is_sat = solver.solve()
        
        print("CL: ", len(model.formula.clauses))
        print("Variables: ", model.formula.nv)
        
        if not is_sat:
            print("UNSAT")
        else:
            result = model.decode_results(solver.get_model())
            solution = model.get_solution(result)
            instance = model.display(solution)

            print(instance)
